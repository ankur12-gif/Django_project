from django.db import models

# Create your models here.
class Books(models.Model):
    book=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    year=models.IntegerField()
    type=models.TextField()
    