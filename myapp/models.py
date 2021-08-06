from django.db import models
#from django.forms import ModelForm

# Create your models here.


class customer(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phone_number = models.IntegerField(10)
    costID = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=50)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.Name


class Book(models.Model):
    publication = models.CharField(max_length=50)
    Isbn_No = models.IntegerField(primary_key=True)
    Author = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    Category = models.CharField(max_length=50, null=True)
    Price = models.IntegerField()
    Edition = models.CharField(max_length=20)
    Qty = models.IntegerField()

    CoverImage = models.ImageField(
        upload_to='static/images/', null=True, blank=True)

    def __str__(self):
        return self.Title
