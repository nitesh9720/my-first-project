from django.db import models
from django.db.models.base import ModelBase

class submitinfo(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    selecttxt=models.CharField(max_length=20)
    checkbox=models.CharField(max_length=10)
    def __str__(self):
        return self.firstname
            # submitdetails=models.CharField(max_length=200)
    # submitdetails=models.TextField()
    # def __str__(self):
    #     return self.firstname

# models for index home page
class oxyzendetail(models.Model):
    suppliername=models.CharField(max_length=50)
    contactnumber=models.CharField(max_length=20)
    area=models.CharField(max_length=50)
    price=models.CharField(max_length=20)
    about=models.CharField(max_length=500)
    def __str__(self):
        return self.suppliername

class carditem(models.Model):
    cardtitle=models.CharField(max_length=100)
    cardtext=models.CharField(max_length=1000)
    cardfooter=models.CharField(max_length=100)

    def __str__(self):
        return self.cardtitle
      