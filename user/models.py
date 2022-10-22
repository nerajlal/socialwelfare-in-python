from django.db import models

# Create your models here.

class addjobdata(models.Model):
    job=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    