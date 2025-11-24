# Ex01 Django ORM Web Application
## Date: 23.11.2025

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Car,CarAdmin
admin.site.register(Car, CarAdmin)

models.py

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


```
## OUTPUT
<img width="1366" height="768" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/01cc0806-a025-4cb2-83db-e3374c799be9" />



## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
 
