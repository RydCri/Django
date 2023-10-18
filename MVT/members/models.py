from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=3, null=True)
    joined_date = models.DateField(null=True)