from django.db import models

class myinfo(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=1000)
    zipCode = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    proCount = models.IntegerField()
    selfDec = models.TextField()

class education(models.Model):
    degreeName = models.CharField(max_length=600,default=None)
    uniName = models.CharField(max_length=600,default=None)
    year = models.CharField(max_length=50,default=None)
    eduDes = models.TextField(default=None)

class experience(models.Model):
    expName = models.CharField(max_length=600,default=None)
    instName = models.CharField(max_length=600,default=None)
    year = models.CharField(max_length=50,default=None)
    expDes = models.TextField(default=None)

class awards(models.Model):
    awardsName = models.CharField(max_length=600, default=None)
    awardsInsName = models.CharField(max_length=600, default = None)
    year = models.CharField(max_length=50, default=None)
    awardsDes = models.TextField(default=None)

class services(models.Model):
    serviceName = models.CharField(max_length=600, default=None)
    experienceYear = models.CharField(max_length=50, default=None)
    reletedTechnology = models.CharField(max_length=600, default = None)
    serviceDes = models.TextField(default=None)