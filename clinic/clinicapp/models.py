from django.db import models

# Create your models here.
class Msg(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    symptoms=models.CharField(max_length=100,default="no")
    description=models.CharField(max_length=100,default="no value")
