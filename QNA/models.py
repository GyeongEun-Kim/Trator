from django.db import models
from django.db.models.base import ModelState
from django.contrib.auth.models import User
from django.conf import settings
from Account.models import CustomUser

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100) #models.ForeignKey(User.username, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "QNA/", blank = True, null = True)
    vote = models.BooleanField(null = True, default=False)

    def __str__(self):
        return self.title

class Answer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    writer = models.CharField(max_length=100) #models.ForeignKey(User.username, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to = "QNA/", blank = True, null = True)
    like = models.BooleanField(null = True, default=False)