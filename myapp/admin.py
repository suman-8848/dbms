from django.contrib import admin
from django.contrib.auth.models import Group,User
from myapp.models import Book, Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['Email','Name','lastName']

class BookAdmin(admin.ModelAdmin):
    list_display = ['Title','Author','Category']
    list_filter = ['Category']


# Register your models here.
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Book,BookAdmin)

#unregister models here
admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.site_header = 'Book Store'