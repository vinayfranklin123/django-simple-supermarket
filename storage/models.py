from django.db import models
from account.models import Account


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    def __str__(self):
        return self.brand_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    product_price = models.FloatField()
    unit_type = models.CharField(max_length=3)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.FloatField()
    def __str__(self):
        return self.product_name


class StockIn(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    quantity_type = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now=True)
    mode = models.CharField(max_length=30)


class StockOut(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    quantity_type = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now=True)
    mode = models.CharField(max_length=30)


class Order(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now=True)


class Items(models.Model):
    item_name = models.CharField(max_length=50, unique=True)
    item_price = models.FloatField()
    item_quantity = models.FloatField()


class Orders(models.Model):
    or_item_name = models.CharField(max_length=50, unique=False)
    or_item_quantity = models.FloatField()
    or_total_price = models.FloatField()
    is_delivered = models.BooleanField(default=False)

