from distutils.command.upload import upload
from email.mime import image
from nturl2path import url2pathname
from pyexpat import model
from django.db import models

# Create your models here.
class Category(models.Model):
    uuid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    url=models.CharField(max_length=500)
    image=models.ImageField(upload_to="media")
    parrent_id=models.ForeignKey("Category",on_delete=models.CASCADE)

class Product(models.Model):
    sku=models.CharField(max_length=100)
    name=models.CharField(max_length=254)
    url=models.CharField(max_length=500)
    price=models.BigIntegerField()
    special_price=models.BigIntegerField()
    images=models.ManyToManyField(Category,related_name='product_image')
    category_ids=models.ManyToManyField(Category,related_name='product_category_id')
    