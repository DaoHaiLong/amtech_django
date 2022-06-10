from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
# urlpatterns = [
#     path('',views.getAllProduct)
    
# ]

urlpatterns = [
    url(r'^$', views.getProductByCategory, name='index'),
    # url(r'^admin/', admin.site.urls),
    
    # -------------------Product------------------------------
    # url(r'^product/(?P<product_id>[0-9]+)/$', views.productbyid, name='product'),
    path('product/<slug:url>/',views.getProductByUrl,name='product'),
    
    # -----------------------Category---------------------------------
    # url(r'^category/(?P<category_url>[a-z]+)/$',views.getProductByCategory,name='product_by_category'),
    # url(r'^category/(?P<category_url>[a-z]/product/(?P<product_id>[0-9]+)/$',views.getProductByCategory,name='product_by_category'),
    path('<slug:category_url>/',views.getProductByCate,name='product_by_category'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)