from django.db import models
from accounts.models import *
from .choices import *

class Base(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(Base):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Product(Base):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            return total_rating / len(reviews)
        return 0

    def __str__(self):
        return f'{self.name}'

class Review(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATINGS, null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.product} - {self.user} - {self.rating}"

        
class ProductImage(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product} - {self.image}"

class Order(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='seller')
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')


    def __str__(self):
        return f"{self.product} - {self.buyer} - {self.status}"
        
        
class Cart(Base):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user}"

class CartItem(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} in {self.cart} - Quantity: {self.quantity}"

