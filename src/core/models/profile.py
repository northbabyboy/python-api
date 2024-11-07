from django.db import models

class User(models.Model):
    username = models.CharField('username', unique=True),
    password = models.CharField('password')