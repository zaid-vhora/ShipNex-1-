from django.contrib import admin
from django.urls import path,include
from app_modules.adminapp import views

urlpatterns = [
    path('index_view/', views.index_view, name='index_view'),
    path('deliveries_view/', views.deliveries_view, name='deliveries_view'),
    path('drivers_view/', views.drivers_view, name='drivers_view'),
    path('login_view/', views.login_view, name='login_view'),
    path('payments_view/', views.payments_view, name='payments_view'),
    path('payments_view/add/', views.payment_add, name='payment_add'),
    path('payments_view/<int:pk>/edit/', views.payment_edit, name='payment_edit'),
    path('payments_view/<int:pk>/delete/', views.payment_delete, name='payment_delete'),
    path('reports_view/', views.reports_view, name='reports_view'),
    path('settings_view/', views.settings_view, name='settings_view'),
    path('shipments_view/', views.shipments_view, name='shipments_view'),
    path('transporters_view/', views.transporters_view, name='transporters_view'),
    path('users_view/', views.users_view, name='users_view'),
    path('vehicles_view/', views.vehicles_view, name='vehicles_view'),
    path('vehicles_view/add/', views.vehicle_add, name='vehicle_add'),
    path('vehicles_view/<int:pk>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('vehicles_view/<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
    path('warehouses_view/', views.warehouses_view, name='warehouses_view'),
    path('warehouses_view/add/', views.warehouse_add, name='warehouse_add'),
    path('warehouses_view/<int:pk>/edit/', views.warehouse_edit, name='warehouse_edit'),
    path('warehouses_view/<int:pk>/delete/', views.warehouse_delete, name='warehouse_delete'),
    path('drivers_view/add/', views.driver_add, name='driver_add'),
    path('drivers_view/<int:pk>/edit/', views.driver_edit, name='driver_edit'),
    path('drivers_view/<int:pk>/delete/', views.driver_delete, name='driver_delete'),
]