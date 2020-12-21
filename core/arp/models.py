from django.db import models
from datetime import datetime
from core.arp.choices import gender_choices
from django.forms import model_to_dict

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    img = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    dni = models.CharField(max_length=10, unique=True)
    birthdate = models.DateField(default=datetime.now)
    address = models.CharField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default='male')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_sale = models.DateField(default=datetime.now)
    sub_total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.total)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    sub_total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']
