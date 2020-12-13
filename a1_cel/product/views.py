from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from shopping_cart.models import Order, OrderItem
from .models import Item


def checkout(request):
    return render(request, "checkout.html")


class StoreView(ListView):
    model = Item
    paginate_by = 10
    template = "store-page.html"


class ProductView(DetailView):
    model = Item
    template = "product.html"

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #To check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, "La cantidad agregada de este producto se ha actualizado")
            return redirect("store:product", slug=slug)
        else:
            order.items.add(order_item)
            messages.success(request, "Este producto fue agregado a tu carrito de compras")
            return redirect("store:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.success(request, "Este producto fue agregado a tu carrito de compras")
        return redirect("store:product", slug=slug)

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    #check if the order item is in the order
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.success(request, "Este producto fue removido de tu carrito de compras")
            return redirect("store:product", slug=slug)
        else:
            messages.info(request, "Este producto no se encuentra en su carrito de compras")
            return redirect("store:product", slug=slug)
    else:
        messages.info(request, "Usted no posee un pedido activo en este momento")
        return redirect("store:product", slug=slug)
    
