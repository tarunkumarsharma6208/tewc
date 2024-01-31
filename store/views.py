from django.shortcuts import render
from .models import *
from accounts.models import *
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