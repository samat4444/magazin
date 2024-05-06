from django.contrib import admin
from .models import Category,Product
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'created', 'updated']
    list_display_links = ['id', 'name',]
    list_filter = ['created', 'updated']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
