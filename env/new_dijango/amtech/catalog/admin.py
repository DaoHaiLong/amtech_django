from django.contrib import admin
from .models import Category,Product
# Register your models here.


class CategoryModelAdmin(admin.ModelAdmin):
    list_filter = ('uuid',)
    prepopulated_fields = {'url': ('name',)} 
    list_display = ('name', 'url','image' )

class ProductModelAdmin(admin.ModelAdmin):
    # readonly_fields = ('image_tag',)   
    prepopulated_fields = {'url': ('name',)} 
    list_display = ('sku', 'name', 'url', 'price','special_price')
admin.site.register(Category,CategoryModelAdmin)
admin.site.register(Product,ProductModelAdmin)