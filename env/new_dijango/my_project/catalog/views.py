from django.shortcuts import render
from django.http import Http404

from .models import Category, Product
# Create your views here.
def index(request):
    # type_objs = Category.objects.all()
    # context = {
    #     'type_objs': type_objs,
    # }
      
    return render(request,'catalogs/categories.html')
    
def product(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'catalogs/product.html', {'product': product})
def category(request):
    data={'Category': Category.objects.all()}
    return render(request,'catalogs/category.html',data)