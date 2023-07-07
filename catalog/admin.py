from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
@admin.register(Product)
class PAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')


@admin.register(Category)
class CAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name', 'description')
