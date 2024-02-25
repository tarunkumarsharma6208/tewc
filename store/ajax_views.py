from accounts.models import *
from .models import *
from django.http import JsonResponse
from django.contrib import messages


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
        
        ad = Address.objects.get(id=id)

        if ad.is_active == False:
            ad.is_active = True
            ad.save()
        elif ad.is_active == True:
            ad.is_active = False
            ad.save()

    return JsonResponse({'message': 'quentity incresed'})

def get_products_query(request):
    l = []
    if request.method == 'GET':
        query = request.GET.get('query')

        obj = Product.objects.filter(name__icontains=query).order_by('name')
        for i in obj:
            l.append(i.name)
    return JsonResponse(l, safe=False)
