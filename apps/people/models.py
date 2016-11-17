from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)

class Interest(models.Model):
    name = models.CharField(max_length=30)
    person = models.ManyToManyField(Person)

# Create your models here.
