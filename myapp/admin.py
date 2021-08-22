from django.contrib import admin
from django.contrib.auth.models import Group,User
from myapp.models import Book, Customer, Order

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['Email','Name','lastName']
    readonly_fields = ['costID','password']
    exclude = [10]

class BookAdmin(admin.ModelAdmin):
    list_display = ['Title','Author','Category','Qty']
    list_filter = ['Category']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_customerID','get_customerName','get_isbn','get_bookTitle','get_price','qty','get_total','get_dateTime']
    readonly_fields = ['book','customer','qty','orderDateTime']
    def regroup_by(self):
        return 'get_customerID'
    def get_customerID(self, obj):
        return obj.customer.costID
    
    def get_customerName(self, obj):
        return (obj.customer.Name + " "+ obj.customer.lastName)
    
    def get_isbn(self, obj):
        return obj.book.Isbn_No

    def get_bookTitle(self, obj):
        return obj.book.Title
    
    def get_price(self, obj):
        return obj.book.Price
    
    def get_total(self,obj):
        return obj.book.Price * obj.qty
    
    def get_dateTime(self,obj):
        return obj.orderDateTime

    get_customerID.short_description = 'Customer ID'
    get_customerName.short_description = 'Customer Name'
    get_isbn.short_description = 'ISBN'
    get_bookTitle.short_description = 'Title'
    get_price.short_description = 'Price'
    get_total.short_description = 'Total'
    get_dateTime.short_description = 'Order date'

    get_customerID.admin_order_field  = 'customer_id'
    get_customerName.admin_order_field  = 'customer_id'



# Register your models here.
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Order,OrderAdmin)

#unregister models here
admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.site_header = 'Book Store'
admin.site.index_title = 'Book Store'
admin.site.site_title = "Admin"