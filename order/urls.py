from django.urls import path
from . import views
from .views import OrderList, OrderView

urlpatterns = [
    path('', views.order_req, name='order-request'),
    path('show/<int:pk>', OrderView.as_view(), name='order-detail'),
    path('show', OrderList.as_view(), name='show-orders')
]