from django.db import models
from accounts.models import *
from .choices import *
from django.utils import timezone
from django.utils.text import slugify

class Base(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(Base):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category/', default='category/jumbo.jpg')
    description = models.TextField(max_length=400)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Brands(Base):
    name = models.CharField(max_length=100, default='NA')
    image = models.ImageField(upload_to='brands/', null=True)

    def __str__(self) -> str:
        return str(self.name)

class Product(Base):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product')
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='product_brand', null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    description = models.TextField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='saller_product')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def is_in_stock(self, quantity=1):
        return self.stock >= quantity

    def discounted_price(self):
        discount_amount = (self.discount_percentage / 100) * self.rate
        return round(self.rate - discount_amount)

    def is_offer_valid(self):
        if self.start_date and self.end_date:
            return timezone.now().date() >= self.start_date and timezone.now().date() <= self.end_date
        return False

    def average_rating(self):
        reviews = self.reviews_product.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            percentage = (total_rating/5)*100
            return round(percentage / len(reviews),1)
        return 0
    def rating_count(self):
        reviews = self.reviews_product.all()
        if reviews:
            return len(reviews)
        else: 
            return 0

    def __str__(self):
        return f'{self.name}'

class Review(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews_product')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATINGS, default=0)
    comment = models.TextField()

    def __str__(self):
        return f"{self.product} - {self.user} - {self.rating}"

        
class ProductImage(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images_product')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product} - {self.image}"

class Order(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='seller_order')
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.product} - {self.buyer} - {self.status}"
        
        
class Cart(Base):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_cartitem')
    items = models.ManyToManyField('CartItem', related_name='carts', blank=True)

    def __str__(self):
        return f"Cart for {self.user}"

class CartItem(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} - {self.quantity}"
    
    def subtotal(self):
        return self.quantity * self.product.rate

class RecentlyViewed(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} viewed {self.product.name}"

    class Meta:
        ordering = ['-timestamp']


class Wishlist(Base):
    name = models.CharField(max_length=100, default='wishlist')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class MainBannerImage(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=100, default='tewc')
    desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image}"