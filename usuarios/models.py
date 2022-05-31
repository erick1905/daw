from __future__ import unicode_literals
from django.conf import settings
from django.db import models

class UsuarioDetalle(models.Model):
    idusuario = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='detalle',on_delete=models.CASCADE)
    direccion = models.CharField(max_length=60, blank=True, null=True) 
    numeroext = models.IntegerField( blank=True, null=True) 
    telefono = models.IntegerField(max_length=10, blank=True, null=True) 
    imagen = models.ImageField(upload_to="perfil/", default = 'images/avatar.png')
    def _str_(self):
        return self.idusuario.username
class Customer(models.Model):
    name=models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    def _str_(self):
        return self.name

class Tag(models.Model):
    name= models.CharField(max_length=200, null=True)
    def _str_(self):
        return self.name

class Product (models.Model):
    CATEGORY =(
        ('Indoor','Indoor'),
        ('Out Door', 'Out Door'),
    )
    name= models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    category= models.CharField(max_length=200, null=True, choices=CATEGORY)
    description= models.CharField(max_length=200, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    tags= models.ManyToManyField(Tag)

    def _str_(self):
        return self.name
    
class Order (models.Model):
    STATUS=(
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product= models.ForeignKey(Product, null=True, on_delete= models.SET_NULL )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS)
    note= models.CharField(max_length=200,null=True)
    def _str_(self) -> str:
        return self.product.name