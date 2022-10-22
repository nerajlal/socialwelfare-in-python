from django.db import models

# Create your models here.
class oldage_members(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    phone=models.IntegerField()
    account=models.IntegerField()
    bank=models.CharField(max_length=100)
    image=models.FileField(upload_to='files')
    oldage_id=models.IntegerField()


class oldage_donation(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    phone=models.IntegerField()
    amount=models.CharField(max_length=50)
    society=models.CharField(max_length=50)
    receive=models.CharField(max_length=50)