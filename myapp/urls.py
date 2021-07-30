from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index),
    path('account',views.account),
    path('index',views.index),
    path('products',views.products),
    path('login',views.login,name='login'),
    
]