from django.contrib import admin
# Register your models here.
from .models import Product, ProductImages, Category, Product_Alternative, Product_Accessories 

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Category)
admin.site.register(Product_Alternative)

admin.site.register(Product_Accessories)

