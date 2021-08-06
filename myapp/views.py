from django.db.models.fields import BooleanField
from myapp.forms import Form
from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def index(request):
    bookdetail = Book.objects.all()
    dict = {
        'books': bookdetail
    }
    return render(request, 'index.html', dict)


def account(request):
    return render(request, 'account.html')


def products(request):
    return render(request, 'products.html')


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

        form = Form(request.POST)

        if form.is_valid():

            try:
                form.save()

                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('Email')
                print(username, raw_password)
                user = User.objects.create_user(
                    username=username,
                    password=raw_password,
                    email=email
                )
                user.is_staff = True
                user.save()
                #user = authenticate(username=username, password=raw_password)
                #login(request, user)
                print(f"data saved\nusername = {user} ")
                return redirect('/account')
            except Exception as e:
                print(e)
    else:
        form = Form()

    return render(request, 'register.html', {'form': form})


def show(request):
    costomers = customer.objects.all()
    return render(request, "show.html", {'costomers': costomers})


# def login(request):
#     if request.method == 'POST':
#         username = request.POST('username')
#         password = request.POST('password')
#         print(username, password)
#         user = authenticate(request, username=username, password=password)

#         if user is not None and user.is_active:
#             auth.login(request, user)
#             if user.is_superuser:
#                 return redirect('myapp:admin')
#             else:
#                 return redirect('myapp:index')
#         else:
#             messages.Info(request, "Invalid username or password")
#             return redirect('myapp:index')


def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("username and password: ", username, password)
            user = authenticate(username=username, password=password)
            print("user", user)
            if user is not None:
                #auth.login(request, user)
               # messages.Info(request, f"You are now logged in as {username}")

                print('successful')
                login(request, user)
                if user.is_superuser:
                    return redirect('admin/')
                return redirect('/')
            else:
                #messages.Info(request, "Invalid username or password")
                print('invalid')
                return redirect('/')
        else:
            # messages.Info(request, "Invalid username or password.")
            print('invalid usr pass')
