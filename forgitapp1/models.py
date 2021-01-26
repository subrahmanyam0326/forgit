from django.db import models

class RegData(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
class LogData(models.Model):
    uname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

