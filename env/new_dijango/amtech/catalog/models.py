from distutils.command.upload import upload
from email.mime import image
from nturl2path import url2pathname
from pyexpat import model
from django.db import models
import django.utils.safestring as safestring
from django.conf import settings
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    uuid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    url=models.CharField(max_length=500)
    image=models.ImageField(upload_to='medias/%Y/%m/%d/')
    parrent_id=models.ForeignKey("Category",on_delete=models.CASCADE,null=True,blank=True)
     
    def image_tag(self):
        if self.image:
            return safestring.mark_safe('<img src="%s%s" width="150" height="150" />' % (settings.MEDIA_URL, self.image))
        else:
            return ""

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('product_by_category',args=[self.url])
        
    def __str__(self):
        return self.name
    

class Product(models.Model):
    sku=models.CharField(max_length=100)
    name=models.CharField(max_length=254)
    url=models.CharField(max_length=500)
    price=models.BigIntegerField()
    special_price=models.BigIntegerField()
    images=models.ManyToManyField(Category,related_name='product_image')
    category_ids=models.ManyToManyField(Category,related_name='product_category_id')
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.url, self.url])
    
    def __str__(self):
        return self.name