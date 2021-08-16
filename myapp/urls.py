from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('account', views.account),
    path('index', views.index),
    path('products', views.products,name = 'products'),
    path('productsd', views.productsd),
    path('register', views.register, name='register'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('show', views.show)
]
