from django.db import models
#from django.forms import ModelForm

# Create your models here.


class Customer(models.Model):
    Name = models.CharField(max_length=20, default=None)
    lastName = models.CharField(max_length=20,default=None)
    Email = models.CharField(max_length=50,default=None)
    phone_number = models.BigIntegerField(default=None)
    costID = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=20,default=None)
    state = models.CharField(max_length=50,default=None)
    postal_code = models.BigIntegerField(default=None)
    password = models.CharField(max_length=100,default=None)

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


class Order(models.Model):
    #orderID = models.IntegerField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    qty = models.IntegerField()
    #totalPrice = models.IntegerField()
    orderDateTime = models.DateTimeField()
    class Meta:
         unique_together = ('id', 'customer', 'book')
