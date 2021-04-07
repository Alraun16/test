from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class New(models.Model):
    user = models.CharField(max_length=30)
    title = models.CharField(max_length=120)
    content = models.TextField()
    publicationDate = models.DateField()
    

    def __str__(self):
        return self.title