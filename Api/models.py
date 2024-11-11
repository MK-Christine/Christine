from django.db import models

# Create your models here.
class users (models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    pnumber = models.IntegerField(max_length=12)

class  article (models.Model):
    name = models.CharField(max_length=40)
    birthdate = models.DateTimeField(blank=True , null=True)


