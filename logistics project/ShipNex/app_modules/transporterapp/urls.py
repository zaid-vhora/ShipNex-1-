app_name = 'transportapp'

from django.contrib import admin
from django.urls import path,include
from app_modules.transporterapp import views

urlpatterns = [
    path('', views.index_view, name='transport_index'),
    path('index_view/', views.index_view, name='index_view'),
    path('assigned_view/', views.assigned_view, name='assigned_view'),
    path('drivers_view/', views.drivers_view, name='drivers_view'),
    path('earnings_view/', views.earnings_view, name='earnings_view'),
    path('pod_view/', views.pod_view, name='pod_view'),
    path('routes_view/', views.routes_view, name='routes_view'),
    path('settings_view/', views.settings_view, name='settings_view'),
    path('shipment_view/', views.shipment_view, name='shipment_view'),
    path('vehicle_view/', views.vehicle_view, name='vehicle_view'),
]
