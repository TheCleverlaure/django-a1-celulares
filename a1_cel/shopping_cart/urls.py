from django.urls import path
from .views import OrderSummaryView

app_name = 'shopping_cart'

urlpatterns = [
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary')
] 