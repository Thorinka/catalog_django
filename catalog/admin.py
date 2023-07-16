from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name', 'category_description',)

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description',)
