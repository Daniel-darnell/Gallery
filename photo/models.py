from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()