from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from Account.models import CustomUser

class Guide (models.Model) :
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    # writer = models.CharField(max_length=10)
    writer = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, related_name="author")
    date = models.DateField()
    location = models.CharField(max_length=10)
    image = models.ImageField( blank=True, null=True, upload_to="guide/")
    price =models.IntegerField()

class Meta :
    db_table = Guide

class MapData(models.Model) :
    #no = models.ForeignKey(Guide,on_delete=models.CASCADE, related_name="mapdata")
    keys =CharField(max_length=1000)
    keysvalues = CharField(max_length=2000)
    cnt = IntegerField(null=True)
class Meta :
    db_table = MapData


# Create your models here.
