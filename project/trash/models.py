from django.db import models
from django.utils import timezone

# Create your models here.
class Trash(models.Model):
    trash_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
