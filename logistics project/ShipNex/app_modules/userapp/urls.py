from django.contrib import admin
from django.urls import path,include
from app_modules.userapp import views

urlpatterns = [
    path('index_view/', views.index_view, name='index_view')
]
