from django.db import models

# Create your models here.
class costomer(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phone_number = models.IntegerField(10)
    costID = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=50)
    postal_code = models.IntegerField()

class Book(models.Model):
    publication = models.CharField(max_length=20)
    Isbn_No = models.IntegerField(primary_key=True)
    Author = models.CharField(max_length=20)
    Title = models.CharField(max_length=20)
    Price = models.IntegerField()
    Edition = models.CharField(max_length=20)
    Qty = models.IntegerField()
    CoverImage = models.ImageField(upload_to = 'static/images/',null=True,blank = True)