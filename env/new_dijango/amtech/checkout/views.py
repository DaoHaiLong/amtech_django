
import imp
import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Quote, Quote_Items
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'checkout/ShoppingCart.html')

def _id(request):
    id=request.session.session_key
    if not id:
        id=request.session.create()
        
def cart(request,subtotal=0,qty=0,admin_fee=3.91,shipping=None,cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = Quote_Items.objects.filter()
        else:
            cart = Quote.objects.get(cart_id=_id(request=request))
            cart_items = Quote_Items.objects.filter(quote=cart)
        for cart_item in cart_items:
            subtotal += cart_item.product.price * cart_item.qty
            qty += cart_item.qty
        if qty<=5:
            shipping=7.5
        else:
            shipping=0
        gst=subtotal*10/100
        order_total=subtotal+shipping+admin_fee+gst
    except ObjectDoesNotExist:
        pass    
    context = {
        'total': subtotal,
        'quantity': qty,
        'cart_items': cart_items,
        'admin_fee':admin_fee,
        'shipping':shipping,
        'tax': gst ,
        'order_total': order_total ,
    }
    return render(request, 'checkout/ShoppingCart.html', context=context)

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
   
    if request.method=='POST':
        for item in request.POST:
            key=item
            value=request.POST.get(key)
    is_exists_cart_item = Quote_Items.objects.filter(product=product).exists()
    if is_exists_cart_item:
        cart_items = Quote_Items.objects.filter(product=product)
        id = [item.id for item in cart_items]
        cart_item=Quote_Items.objects.get(id)
        cart_item.qty +=1
    else:
        cart_item = Quote_Items.objects.create(product=product,qty=1)
    cart_item.save()
    return redirect('cart')


def remove_cart_item(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = Quote_Items.objects.get(
                id=cart_item_id,
                product=product,
            )
        else:
            cart = Quote.objects.get(cart_id=_id(request=request))
            cart_item = Quote_Items.objects.get(
                id=cart_item_id,
                product=product,
                quote=cart
            )
        cart_item.delete()
    except Exception:
        pass
    return redirect('cart')

def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = Quote_Items.objects.get(
                id=cart_item_id,
                product=product,
            )
        else:
            cart = Quote.objects.get(cart_id=_id(request))
            cart_item = Quote_Items.objects.get(
                id=cart_item_id,
                product=product,
                quote=cart
            )
        if cart_item.qty > 1:
            cart_item.qty -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except Exception:
        pass
    return redirect('cart')

def add_cart_qty(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = Quote_Items.objects.get(
                id=cart_item_id,
                product=product,
            )
        else:
            cart = Quote.objects.get(cart_id=_id(request))
            cart_item = Quote_Items.objects.get(
                id=cart_item_id,
                product=product,
                quote=cart
            )
        if cart_item.qty:
            cart_item.qty += 1
            cart_item.save()
        else:
            cart_item.delete()
    except Exception:
        pass
    return redirect('cart')