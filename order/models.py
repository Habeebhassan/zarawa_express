from django.db import models
from django.contrib.auth.models import User
from bulma_widget import widgets

# Create your models here.

class Order(models.Model):
    
    name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    pickup_address = models.CharField(max_length=200, blank=True)
    pickup_name = models.CharField(max_length=100, blank=True)
    pickup_phone = models.CharField(max_length=30, blank=True)
    dropoff_address = models.CharField(max_length=200, blank=True)
    recipient_name = models.CharField(max_length=100, blank=True)
    recipient_phone = models.CharField(max_length=30, blank=True)
    order_details = models.TextField()
    submitted = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)
