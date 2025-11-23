from django.db import models
from django.contrib import admin

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.FloatField()



class CarAdmin(admin.ModelAdmin):
    
    list_display = ('model_name', 'brand', 'year', 'mileage', 'price')