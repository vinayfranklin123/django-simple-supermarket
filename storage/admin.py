from django.contrib import admin
from storage.models import Items, Orders, Brand, Category, Product, StockOut, StockIn

admin.site.register(Items)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(StockIn)
admin.site.register(StockOut)


# Register your models here.
