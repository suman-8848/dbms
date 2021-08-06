from django.contrib import admin
from myapp.models import Book, customer
# Register your models here.
admin.site.register(customer)
admin.site.register(Book)
