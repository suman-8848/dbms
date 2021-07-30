from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request,'index.html')
def account(request):
    return render(request,'account.html')
def products(request):
    return render(request,'products.html')
def productdetails(request):
    return render(request,'product-details.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username= username, password= password)
        if user is not None and user.is_active:
            auth.login(request,user)
            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('index')
        else:
            messages.Info(request,"Invalid username or password")
            return redirect('index')
        