from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/',views.search,name="search"),
    path('signin/', views.signin, name="signin"),
    path('login/', views.handlelogin, name="handlelogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
]

    

