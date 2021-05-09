from django import forms
from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    required_css_class ='required'
    class Meta:
        model = Order
        fields = [
            'name', 'phone_number', 'order_details', 'pickup_name', 
            'pickup_address', 'pickup_phone', 'recipient_name', 
            'dropoff_address', 'recipient_phone'
        ]