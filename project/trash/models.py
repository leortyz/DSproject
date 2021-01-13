from django.db import models

# Create your models here.
class Trash(models.Model):
    trash_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Image(models.Model):
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    img = models.BinaryField()
    pub_date = models.DateTimeField('date published')
