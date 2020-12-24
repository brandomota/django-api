from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True,max_length=100)
    cpf = models.CharField(unique=True,max_length=14)
    password = models.CharField(max_length=255)

