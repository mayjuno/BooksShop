from email.policy import default
from operator import mod
from re import T
from django.db import models

# Create your models here.
class Book(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )  
    title = models.CharField(max_length=256)
    isbn = models.CharField(max_length=30)
    publishedDate = models.DateTimeField(auto_now_add=True)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256,null=True)
    shortDescription = models.CharField(max_length=256,null=True)
    longDescription = models.TextField(null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    status = models.CharField(max_length=10,choices=STATUS,default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title