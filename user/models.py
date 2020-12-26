from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(unique=True,max_length=100, null=False, blank=False)
    cpf = models.CharField(unique=True,max_length=11, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'users'

