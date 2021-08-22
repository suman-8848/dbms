import myapp
from django.db.models.fields import BooleanField
#from myapp.forms import Form
from django.core.checks import messages
from django.http.response import HttpResponse, JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from mysite import settings
import time
from datetime import datetime
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
# Create your views here.

#selectedBooks = None
search = None

def index(request):
    bookdetail = Book.objects.all()
    dict = {
        'books': bookdetail
    }
    request.session['cart'] = {}
    return render(request, 'index.html', dict)


def account(request):
    return render(request, 'account.html')


def products(request):
    
    try:
        global search
        search = request.POST['search']
    except:
        print("Search is none.")
    if search:
        searched = Book.objects.filter(Title__icontains = search)
        dict = {
            'books': searched,
            'search':True

        }
    else:
        bookdetail = Book.objects.all()
        dict = {
            'books': bookdetail,
            'search': False
        }
    if request.POST.get('Isbn') is not None:
        cart(request)

    return render(request, 'products.html',dict)


def productsd(request):
    bookdetail = Book.objects.all()
    dict = {
        'books': bookdetail
    }
    return render(request, 'productsd.html', dict)


def productdetails(request):
    return render(request, 'product-details.html')


def register(request):

    if request.method == "POST":
        data = request.POST
        customer = Customer()
        customer.costID = time.time()
        customer.Name = data['first_name']
        customer.lastName = data['last_name']
        customer.city = data['city']
        customer.state = data['state']
        customer.postal_code = data['postal_code']
        customer.Email = data['email']
        customer.phone_number = data['phone_number']
        customer.password = data['password']
        confirmedPassword = data['confirm_password']

        err = None
        if " " in customer.Name or " " in customer.lastName or " " in customer.city[0] or " " in customer.state or " " in customer.Email:
            err = "Fields cannot contain spaces."
        elif (not customer.Name.isalpha()) or (not customer.lastName.isalpha()):
            err = "First name and last name cannot contain digits and special characters."
        elif Customer.objects.filter(Email = customer.Email):
            err = "Email already registered."
        elif not customer.city.isalpha():
            err = "City cannot contain numbers and special characters."
        elif len(customer.phone_number)<10:
            err = "Phone number invalid."
        elif customer.password != confirmedPassword:
            err = "Passwords do not match."
        
        if not err:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('products')
        else:
            context = {
                'err':err,
                'data':{'first_name':customer.Name,
                        'last_name':customer.lastName,
                        'city':customer.city,
                        'postal_code':customer.postal_code,
                        'state':customer.state,
                        'phone_number':customer.phone_number,
                        'email':customer.Email}
            }
            return render(request,'register.html',context)

    return render(request,'register.html')


def show(request):
    costomers = Customer.objects.all()
    return render(request, "show.html", {'costomers': costomers})


def userlogin(request):
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']

        #authenticate admin
        user = authenticate(username=email, password=password)

        err = None

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
        else:
            customer = None
            try:
                customer = Customer.objects.get(Email = email)
                request.session['email'] = email
                #print(customer.password)
            except:
                err = "Email/Username or password incorrect."
            
            if (customer is not None) and check_password(password, customer.password):
                return redirect('products')
        
        
        return render(request,'account.html',{'err':err})

# def search(request):
#     search = request.POST['search']
#     searched = Book.objects.filter(Title__icontains = search)
#     dict = {
#         'books': searched

#     }
#     return render(request,'search.html',dict)

# def userlogin(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print("username and password: ", username, password)
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect(request.GET.get('next',
#                                             settings.LOGIN_REDIRECT_URL))
#             else:
#                 error = 'Invalid username or password.'
#             print("user", user)
#             if user is not None:
#                 #auth.login(request, user)
#                # messages.Info(request, f"You are now logged in as {username}")

#                 print('successful')
#                 login(request, user)
#                 if user.is_superuser:
#                     return redirect('admin/')
#                 return redirect('/')
#             else:
#                 #messages.Info(request, "Invalid username or password")
#                 print('invalid')
#                 return redirect('/')
#         else:
#             # messages.Info(request, "Invalid username or password.")
#             print('invalid usr pass')

def cart(request):
    ISBN = request.POST['Isbn']
    cartObject = request.session.get('cart')
    if cartObject:
        if cartObject.get(ISBN):
            cartObject[ISBN] += 1
        else:
            cartObject[ISBN] = 1
    else:
        cartObject = {}
        cartObject[ISBN] = 1
    request.session['cart'] = cartObject

def checkout(request):
    books = []
    for k in request.session.get('cart'):
        books.append(Book.objects.get(Isbn_No = k))

    context = {
        'books':books
    }
    return render(request,'checkout.html',context)


def order(request):
    if request.method == "POST":
        currTime = datetime.now()
        for k,v in request.session['cart'].items():
            order = Order()
            book = Book.objects.get(Isbn_No = k)
            order.book = book
            order.qty = v
            book.Qty -= v
            order.customer = Customer.objects.get(Email = request.session['email'])
            order.orderDateTime = currTime
            order.save()
        book.save()

        return render(request,'thankyou.html')
    else:
        return HttpResponse("403 Forbidden")