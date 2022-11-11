from django.contrib import admin

from mainapp.models import Product, ProductCategory

admin.site.admin.site.register(Product)
admin.site.admin.site.register(ProductCategory)
