from accounts.models import *
from .models import *
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect


def increse_prod_quentity(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        quentity = request.GET.get('quentity')

        product = Product.objects.get(id=product_id)

        # cart = Cart.objects.get(user=request.user)

        # Get or create the cart item for the product
        cart_item = CartItem.objects.get(product=product)

        # If the item is already in the cart, increment the quantity
        
        cart_item.quantity = int(quentity)
        cart_item.save()
        

        # # Associate the cart item with the user's cart
        # cart.items.add(cart_item)
    return JsonResponse({'message': 'quentity incresed'})

def activate_addtess(request):
    if request.method == 'GET':
        id = request.GET.get('address_id')
        
        Address.objects.filter(user=request.user).update(is_active=False)

        Address.objects.filter(id=id, user=request.user).update(is_active=True)
        # default = ad.get(id=id)
        # if default.is_active == False:
        #     default.is_active = True
        #     default.save()
        # elif default.is_active == True:
        #     default.is_active = False
        #     default.save()

    return JsonResponse({'message': 'quentity incresed'})

def get_products_query(request):
    l = []
    if request.method == 'GET':
        query = request.GET.get('query')

        obj = Product.objects.filter(name__icontains=query).order_by('name')
        for i in obj:
            l.append(i.name)
    return JsonResponse(l, safe=False)


def add_to_cart(request):
    # Get the product
    if request.user.is_authenticated:
        if request.method == 'GET':
            product_id = request.GET.get('product_id')
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
            msg = f'{product.name} has been added to your cart'
            return JsonResponse({'message': msg})
        else:
            return JsonResponse({'message': "somthings went wrong"})

    else:
        return JsonResponse({'message': 'Please login first!'})


# @login_required(login_url='/account/login/')
def add_to_wishlist(request):
    # Get the product
    if request.user.is_authenticated:
        if request.method == 'GET':
            product_id = request.GET.get('product_id')
            # print(product_id, '==================')
            product = get_object_or_404(Product, pk=product_id)

            if Wishlist.objects.filter(user=request.user, product=product).exists():
                msg = f'Already this product exist in wishlist'
                return JsonResponse({'message': msg, 'type': 'info'})
            else:
                # Check if the user already has a wishlist
                Wishlist.objects.create(user=request.user, product=product)

                msg = f'{product.name} has been added to your wishlist'
                return JsonResponse({'message': msg, 'type': 'success'})
        else:
            return JsonResponse({'message': "somthings went wrong", 'type': 'error'})

    else:
        return JsonResponse({'message': 'Please login first!', 'type': 'error'})
    

def add_to_recently_view(request):
    # Get the product
    if request.user.is_authenticated:
        if request.method == 'GET':
            product_id = request.GET.get('product_id')
            # print(product_id, '==================')
            product = get_object_or_404(Product, pk=product_id)

            if RecentlyViewed.objects.filter(user=request.user, product=product).exists():
                
                return JsonResponse({'message': '', 'type': 'info'})
            else:
                # Check if the user already has a wishlist
                RecentlyViewed.objects.create(user=request.user, product=product)

                return JsonResponse({'message': '', 'type': 'success'})
        else:
            return JsonResponse({'message': "somthings went wrong", 'type': 'error'})

    else:
        return JsonResponse({'message': 'Please login first!', 'type': 'error'})