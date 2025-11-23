from django.db import models
from django.contrib import admin
class product(models.Model):
    productname=models.CharField(primary_key=True,max_length=30)
    ProductID=models.CharField(max_length=30)
    category=models.CharField(max_length=10)
    Description=models.CharField(max_length=200)
    stock=models.IntegerField()
    price=models.IntegerField()
class productAdmin(admin.ModelAdmin):
    list_display=["productname","ProductID","category","Description","stock","price"]


