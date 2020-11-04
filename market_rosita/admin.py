from django.contrib import admin
from .models import Brand, Category, Product

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', 'stock', 'price', 'id_brand', 'id_category')

# Register your models here.
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)