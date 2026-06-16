from django.contrib import admin
from django.urls import path,include
from app_modules.adminapp import views

urlpatterns = [
    path('index_view/', views.index_view, name='index_view'),
    path('deliveries_view/', views.deliveries_view, name='deliveries_view'),
    path('drivers_view/', views.drivers_view, name='drivers_view'),
    path('login_view/', views.login_view, name='login_view'),
    path('payments_view/', views.payments_view, name='payments_view'),
    path('reports_view/', views.reports_view, name='reports_view'),
    path('settings_view/', views.settings_view, name='settings_view'),
    path('shipments_view/', views.shipments_view, name='shipments_view'),
    path('transporters_view/', views.transporters_view, name='transporters_view'),
    path('users_view/', views.users_view, name='users_view'),
    path('vehicles_view/', views.vehicles_view, name='vehicles_view'),
    path('warehouses_view/', views.warehouses_view, name='warehouses_view'),
]