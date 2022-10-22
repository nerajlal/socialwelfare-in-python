from django.db import models

# Create your models here.
class women_members(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.CharField(max_length=50)
    status1=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    phone=models.IntegerField()
    account=models.IntegerField()
    bank=models.CharField(max_length=100)
    image=models.FileField(upload_to='files')
    women_id=models.IntegerField()

class women_proposal(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField()
    occupation=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    image=models.FileField(upload_to='files')
    women=models.CharField(max_length=50)
    welfare=models.CharField(max_length=50)

class women_product(models.Model):
    society_id=models.IntegerField()
    pname=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.FileField(max_length=50)

class women_purchase(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    item=models.CharField(max_length=50)
    society=models.CharField(max_length=50)


class women_donation(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    amount=models.CharField(max_length=50)
    society=models.CharField(max_length=50)
    receive=models.CharField(max_length=50)