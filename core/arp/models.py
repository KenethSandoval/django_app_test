from django.db import models
from datetime import datetime


class Type(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Employee (models.Model):
    type = models.ForeignKey(Type, models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    dni = models.CharField(max_length=10, unique=True)
    date_joined = models.DateField(default=datetime.now)
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    gender = models.CharField(max_length=10)
    cvitae = models.FileField(upload_to='avatar/%Y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
