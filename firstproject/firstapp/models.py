from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=255)
    product_price=models.FloatField()

    def __str__(self):
        return self.product_name

    @classmethod
    def create(cls,product_name, product_price):
        product=Product(product_name=product_name, product_price=product_price)
        product.save()
        return product

    @classmethod
    def updatePrice(cls,product_id, product_price):
        product=cls.objects.filter(product_id=product_id)
        product=product.first()
        product.product_price0=product_price
        product.save()
        return product
        

class CreateCart(models.Manager):
    def create_cart(self, user):
        cart= self.create(user=user)
        return cart

class Cart(models.Model):
    card_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField()
    objects=CreateCart()

class ProductInCart(models.Model):
    class Meta:
        unique_together=(('cart','product'),) #it is a composite key which should be unique
    product_in_cart_id=models.AutoField(primary_key=True)
    cart=models.OneToOneField(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

class Order(models.Model):
    status_chocies=(
        (1,'Not Packed'),
        (2,'Ready for shipment'),
        (3,'shipped'),
        (4,'Delivered'),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    choices=models.IntegerField(choices=status_chocies, default=1)

class Deals(models.Model):
    user=models.ManyToManyField(User)
    deal_name=models.CharField(max_length=50)


