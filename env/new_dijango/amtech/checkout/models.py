
from django.db import models
from catalog.models import Product

# Create your models here
class Quote(models.Model):
    subtotal=models.BigIntegerField()
    shipping=models.CharField(max_length=500)
    admin_fee=models.DecimalField(max_digits=5,decimal_places=3)
    gst=models.DecimalField(max_digits=5,decimal_places=3)
    order_total=models.DecimalField(max_digits=5,decimal_places=3)
    def __str__(self):
        return str(self.id)

class Quote_Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quote=models.ForeignKey(Quote,on_delete=models.CASCADE,null=True,blank=True)
    qty=models.IntegerField()
    
    
    def sub_total(self):
        total=self.qty * self.product.price
        return total
        
    def  __unicode__(self):
        return self.product