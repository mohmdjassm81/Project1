from tkinter import CASCADE
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from django.urls import reverse
from  django.utils.text import slugify
# Create your models here.

from django.urls import reverse


class Product(models.Model):
    ## معلومات المنتج
    PRDName = models.CharField(max_length=100, verbose_name='اسم المنتج')
    PRDCategory = models.ForeignKey('Category' , on_delete=models.CASCADE , blank=True , null=True)
    PRDPrand = models.ForeignKey('settings.Brand' , on_delete=models.CASCADE , blank=True , null=True)


    PRDDesc = models.TextField(max_length=500)

    PRDImage = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='صور المنتج')
    PRDSImage1 = models.ImageField(upload_to='products1/', blank=True, null=True, verbose_name='1صور صغيرة للمنتج')
    PRDSImage2 = models.ImageField(upload_to='products2/', blank=True, null=True, verbose_name='2صور صغيرة للمنتج')
    PRDSImage3 = models.ImageField(upload_to='products3/', blank=True, null=True, verbose_name='3صور صغيرة للمنتج')



    PRDPrice = models.DecimalField(max_digits=10, decimal_places=5)
    PRDCost = models.DecimalField(max_digits=10, decimal_places=5)

    PRDCreated = models.DateTimeField()
    PRDSLug = models.SlugField(blank=True , null=True)

   




    def save(self , *args , **kwargs):
        if not self.PRDSLug:
            self.PRDSLug = slugify(self.PRDName)
        super(Product , self).save(*args , **kwargs)

    def get_absolute_url(self):

        return  reverse('products:product_detail', kwargs = {'slug':self.PRDSLug} )


    def __str__(self):
        return self.PRDDesc


class ProductImages(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='صورة المنتج')
    PRDIImage = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='صور المنتج')

    def __str__(self):
        return str(self.PRDName)













class Category(models.Model):
    CATName = models.CharField(max_length=50)
    CATParent = models.ForeignKey('self', limit_choices_to={'CATParent__isnull': True}, on_delete=models.CASCADE,blank=True, null=True)
    CATDesc = models.TextField()
    CATImg = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.CATName


class Product_Alternative(models.Model):
    ## for product brand
    PALNProduct = models.ForeignKey(Product , on_delete= models.CASCADE , related_name= 'main_prodcut')
    PALNAlternatives = models.ManyToManyField(Product , related_name='alternative_products') 
    

    class Meta:
        verbose_name = 'Product Alternative'
        verbose_name_plural = 'Product Alternatives'

    def __str__(self):
        return str(self.PALNProduct)



class Product_Accessories(models.Model):
    
    PACCProduct = models.ForeignKey(Product , on_delete= models.CASCADE , related_name= 'mainAccessory_prodcut')
    PACCAlternatives = models.ManyToManyField(Product , related_name='accessories_products') 
    

    class Meta:
        verbose_name = 'Product Accessory'
        verbose_name_plural = 'Product Accessories'

    def __str__(self):
        return str(self.PACCProduct)




