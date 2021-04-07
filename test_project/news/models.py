from django.db import models
from datetime import date

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    publicationDate = date.datetime()
    