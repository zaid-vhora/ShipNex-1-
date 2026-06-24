from django.contrib import admin
from django.urls import path, include
from app_modules.userapp import views



urlpatterns = [
    # Homepage
    path('', views.index_view, name='user_home'),
    path('index/', views.index_view, name='user_index'),
    
    # Authentication
    path('login/', views.login_view, name='user_login'),
    path('register/', views.register_view, name='user_register'),
    
     # Dashboard & Shipment Management
    path('dashboard/', views.dashboard_view, name='user_dashboard'),
    path('create-shipment/', views.create_shipment_view, name='create_shipment'),
    path('cancel-shipment/<int:shipment_id>/', views.cancel_shipment_view, name='cancel_shipment'),
    path('track-shipment/<str:tracking_number>/', views.track_shipment_json, name='track_shipment_json'),
    
    # Public Pages
    path('about/', views.about_view, name='user_about'),
    path('services/', views.services_view, name='user_services'),
    path('contact/', views.contact_view, name='user_contact'),
    path('tracking/', views.tracking_view, name='user_tracking'),
]
