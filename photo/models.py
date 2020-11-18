from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=30)
    post = models.TextField()
    category = models.CharField(max_length=30)
    editor = models.ForeignKey(Editor)

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name