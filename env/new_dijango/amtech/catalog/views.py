from re import T
from telnetlib import STATUS
from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    products = Product.objects.all()
    type_objs = Category.objects.filter()
    context = {
        'type_objs': type_objs,
        'products':products,
    }
      
    return render(request,'catalog/categorypage.html',context)
    
def productbyid(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'catalog/products.html', {'product': product})

def getProductByUrl(request,url):
    try:
        product = Product.objects.get(url=url)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'catalog/products.html', {'product': product})

def category(request):
    data={'Category': Category.objects.all()}
    return render(request,'catalog/categories.html',data)

def PageCategory(request):
    type_objs = Category.objects.filter()
    return render(request,'catalog/categorypage.html')


def getProductByCategory(request,category_url=None):
    type_objs = Category.objects.filter()
    if category_url is not None:
        categories=get_object_or_404(Category,url=category_url)
    product=Product.objects.all().filter()
    
    # pagination 
    page = request.GET.get('page', 1)

    paginator = Paginator(product, 8)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    # else:
    #     product = Product.objects.all().filter(category_ids=True).order_by('id')
    # page= request.GET.get('page')
    context = {
        # 'category': category,
        'product':product,
        'type_objs': type_objs,
        'page_obj':page_obj
    }

    return render(request,'catalog/categorypage.html',context)
    
def getProductByCate(request,category_url):
    type_objss = Category.objects.filter(url=category_url)
    
    if type_objss :
        # categories=get_object_or_404(Category,url=category_url)
        productcate=Product.objects.all().order_by()
    # else:
    #     product = Product.objects.all().filter(category_ids=True).order_by('id')
    
    # paginator = Paginator(productcate, per_page=2)
    # page_object=paginator.get_page(page)
    # page_object.adjusted_elided_pages=paginator.get_elided_pade_range(page)
    paginator=Paginator(productcate,8)
    page=request.GET.get('page',1)
    
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        page_obj = paginator.page(paginator.num_pages)
    
    
    context = {
        # 'category': category,
        'productcate':productcate,
        'type_objs': type_objss,
        'page_obj':page_obj
    }

    return render(request,'catalog/productbycate.html',context)