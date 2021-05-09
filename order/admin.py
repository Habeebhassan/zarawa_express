from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'submitted')
    list_filter = ('name', 'submitted')
    readonly_fields = ('submitted',)

    fieldsets = (
        (None, {'fields': ('name', 'phone_number', 'order_details')
        }),
        ('Pick-Up Details', {
            'classes': ('collapse',),
            'fields': ('pickup_name', 'pickup_address', 'pickup_phone')
        }),
        ('Recipient Details', {
            'classes': ('collapse',),
            'fields': ('recipient_name', 'dropoff_address', 'recipient_phone', 'submitted')
        }),
        ('Order Admin', {
            'classes': ('collapse',),
            'fields': ('username',)
        })
    )


admin.site.register(Order, OrderAdmin)
