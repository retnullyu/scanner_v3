#coding=utf-8
from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta():
        db_table='users_db'