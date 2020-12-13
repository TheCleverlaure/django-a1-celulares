from django.urls import path
from .views import checkout, StoreView, ProductView, add_to_cart, remove_from_cart


app_name = 'store'

urlpatterns = [
    path('', StoreView.as_view(template_name='store-page.html'), name='store'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ProductView.as_view(template_name='product.html'), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart')
]
