
from django.contrib import admin
from django.urls import path
from django.urls import include
from blog import views

urlpatterns = [
    path('', views.blogpage,name="blogpage"),
    path('<slug:slug>/', views.blogPost, name="blogPost"),   
   
]
