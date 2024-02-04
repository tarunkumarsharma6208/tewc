from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from accounts.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {}
    banner = MainBannerImage.objects.first()
    products = Product.objects.all()
    f =  products.first().images_product.all()
    print(f)
    category = Category.objects.all()
    # latest_product = Product.objects.latest('created_at')
    latest_products = Product.objects.order_by('-created_at')[:100]


    context.update({'banner': banner, 'products': products, 'category': category, 'latest_products': latest_products})
    return render(request, 'store/home/index.html.j2', context)

def products_list(request, category):
    context = {}
    print(category, 9999999999999999999999999999999999999)
    products = Product.objects.filter(category__slug=category)
    print(11111111111, products, '0000000000000000000000000000')
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
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.select_related('cart','product').filter(cart=cart)
    print(cart_items)
    return render(request, 'store/cart/cart.html.j2', {'cart_items': cart_items})

# @login_required
def add_to_cart(request, product_id):
    # Get the product
    product = get_object_or_404(Product, pk=product_id)

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the item is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    # If the item is already in the cart, increment the quantity
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')

def checkout(request):
    context = {

    }
    return render(request, 'store/checkout/checkout.html.j2', context)


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
    wish_list = Wishlist.objects.get(user=request.user)
    context.update({
        'wish_list':wish_list,
    })
    return render(request, 'store/wishlist/wishlist.html.j2', context)

