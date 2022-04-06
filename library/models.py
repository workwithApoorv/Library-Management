import datetime
from tkinter import CASCADE
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=30)
    book_sn = models.CharField(max_length=3)
    rented = models.IntegerField(default=0, editable=False)
    book_date=models.DateField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self) -> str:
        return self.book_name