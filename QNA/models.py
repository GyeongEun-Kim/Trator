from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    writer =  models.CharField(max_length=50) #models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "QNA/", blank = True, null = True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    title = models.ForeignKey(Question, on_delete=models.CASCADE)
    writer =  models.CharField(max_length=50) #models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to = "QNA/", blank = True, null = True)