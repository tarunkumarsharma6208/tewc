from django.contrib import admin
from .models import *

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product, ProductAdmin)

admin.site.register(Review)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.register(RecentlyViewed)
admin.site.register(Wishlist)
admin.site.register(MainBannerImage)

admin.site.register(Brands)


# Register your models here.
