from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatGroup(models.Model):
    name = models.CharField(max_length=100)

class Chat(models.Model):
    content = models.CharField(max_length=199)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)

