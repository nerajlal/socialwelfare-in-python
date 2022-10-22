from django.db import models

# Create your models here.


class register(models.Model):
    category=models.CharField(max_length=100)
    society=models.CharField(max_length=100)
    manager=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    phone=models.IntegerField()
    account=models.IntegerField()
    bank=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    status=models.BooleanField(default=0)
    
    