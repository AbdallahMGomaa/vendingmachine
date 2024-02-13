from django.contrib import admin
from crm.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount_available', 'cost', 'seller_id']
    readonly_fields = ('id',)
