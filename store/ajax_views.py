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
        if product.stock <= int(quentity):
            cart_item.quantity = int(quentity)
            cart_item.save()
        else:
            messages.warning(request, 'Product Out of Stock')

        # # Associate the cart item with the user's cart
        # cart.items.add(cart_item)
    return JsonResponse({'message': 'quentity incresed'})