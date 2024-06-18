from django.db import models

# Create your models here.
Class Post(models.Model):
    title=models.CharField(max_length=250)
    slud=models.SlugField(max_length=250)
    body=models.TextField()

    def __str__(self):
        return self.title
