from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from accounts.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.db.models import F, ExpressionWrapper, DecimalField
from django.contrib import messages
# Create your views here.

def index(request):
    context = {}
    banner = MainBannerImage.objects.first()
    products = Product.objects.all()
    f =  products.first().images_product.all()
    # print(f)
    category = Category.objects.all()
    # latest_product = Product.objects.latest('created_at')
    latest_products = Product.objects.order_by('-created_at')[:100]
    trending_products = Product.objects.annotate(num_wishlists=Count('wishlist')).order_by('num_wishlists')[:10]
    top_rated_products = Product.objects.annotate(avg_rating=Avg('reviews_product__rating')).order_by('avg_rating')[:4]

    top_discounted_products = Product.objects.annotate(
        discounted=ExpressionWrapper(
            F('rate') - (F('rate') * F('discount_percentage') / 100),
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )
    ).order_by('discounted')[:6]

    brands = Brands.objects.all().order_by('id')[:6]
    print(trending_products)
    context.update({'banner': banner, 'brands':brands, 'products': products, 'category': category, 'top_discounted_products': top_discounted_products, 'top_rated_products':top_rated_products, 'latest_products': latest_products, 'trending_products': trending_products})
    return render(request, 'store/home/index.html.j2', context)

def products_list(request, category):
    context = {}
    # print(category, 9999999999999999999999999999999999999)
    products = Product.objects.filter(category__slug=category)
    # print(11111111111, products, '0000000000000000000000000000')
    context.update({'products': products})
    return render(request, 'store/home/products-list.html.j2', context)

def product_detail(request, product_slug):
    context = {}
    product = Product.objects.get(slug=product_slug)
    context.update({
        'product':product,
    })
    return render(request, 'store/home/products-detail.html.j2', context)

# @login_required
def cart_view(request):
    # cart = get_object_or_404(Cart, user=request.user)
    cart_items = Cart.objects.get(user=request.user)
    price = 0
    if cart_items:
        products_list = cart_items.items.all()
        for i in products_list:
            price += i.subtotal()
    


    print(price, '=================')
    print(cart_items)
    return render(request, 'store/cart/cart.html.j2', {'cart_items': cart_items, 'total_price': price})

# @login_required
def add_to_cart(request, product_id):
    # Get the product
    product = get_object_or_404(Product, pk=product_id)

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Get or create the cart item for the product
    cart_item, item_created = CartItem.objects.get_or_create(product=product)

    # If the item is already in the cart, increment the quantity
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    # Associate the cart item with the user's cart
    cart.items.add(cart_item)

    return redirect('cart_view')

def remove_from_cart(request, product_id):
    # Get the product
    product = get_object_or_404(Product, pk=product_id)

    # Get or create the user's cart
    cart = Cart.objects.get(user=request.user)

    # Get or create the cart item for the product
    cart_item = CartItem.objects.get(product=product)

    cart_item.delete()

    cart.items.remove(cart_item)

    return redirect('cart_view')

def checkout(request):
    context = {

    }
    return render(request, 'store/checkout/checkout.html.j2', context)

@login_required(login_url='/account/login/')
def add_to_wishlist(request, product_id):
    # Get the product
    product = get_object_or_404(Product, pk=product_id)

    # Check if the user already has a wishlist
    wish_item, created = Wishlist.objects.get_or_create(user=request.user)

    # Add the product to the wishlist
    wish_item.products.add(product)

    return redirect('wishlist_view')

def wishlist_view(request):
    context = {}
    wish_list = Wishlist.objects.filter(user=request.user)
    context.update({
        'wish_list':wish_list,
    })
    return render(request, 'store/wishlist/wishlist.html.j2', context)


def order_tracking(request):
    context = {}

    return render(request, 'store/order/order-tracking.html.j2', context)



#=====admin section ===========
def store_admin(request):
    context = {}
    order = Order.objects.all()
    context.update({'order': order})
    return render(request, 'admin/home.html.j2', context)

