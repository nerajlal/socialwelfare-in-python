from django.db import models
from django.forms import EmailInput

# Create your models here.
class orphanage_members(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    talent=models.CharField(max_length=100)
    disability=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    account=models.CharField(max_length=100)
    bank=models.CharField(max_length=100)
    image=models.FileField(upload_to='files')
    orphanage_id=models.IntegerField()


class orphanage_product(models.Model):
    society_id=models.IntegerField()
    pname=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.FileField(max_length=50)
  
class orphanage_purchase(models.Model):
    society=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    item=models.CharField(max_length=50)

class orphanage_adoption(models.Model):
    child_id=models.IntegerField()
    name=models.CharField(max_length=50)
    marital=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    reason=models.CharField(max_length=500)
    society=models.CharField(max_length=50)

class orphanage_sponsor(models.Model):
    child_id=models.IntegerField()
    name=models.CharField(max_length=50)
    marital=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    society=models.CharField(max_length=50)

class orphanage_donation(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    amount=models.CharField(max_length=50)
    society=models.CharField(max_length=50)
    receive=models.CharField(max_length=50)




    



    
    
    
    




