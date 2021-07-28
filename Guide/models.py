from django.db import models

class Guide (models.Model) :
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    writer = models.CharField(max_length=10)
    date = models.DateField()
    location = models.CharField(max_length=10)
    image = models.ImageField( blank=True, null=True, upload_to="guide/")
    price =models.IntegerField()

class Meta :
    db_table = Guide
# Create your models here.
