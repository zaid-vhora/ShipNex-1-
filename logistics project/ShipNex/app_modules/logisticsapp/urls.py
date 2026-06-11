from django.contrib import admin
from django.urls import path, include
from app_modules.logisticsapp import views

urlpatterns = [
    path('', views.logistics_Dashboard_view, name='dashboard'),
    path('logistics_Dashboard_view/', views.logistics_Dashboard_view, name='logistics_Dashboard_view'),
    path('shipment-management/', views.Shipment_Management_view, name='shipment_management'),
    path('shipment-tracking/', views.shipment_tracking_view, name='shipment_tracking'),
    path('vehicle-assignment/', views.vehicle_assignment_view, name='vehicle_assignment'),
    path('driver-assignment/', views.driver_assignment_view, name='driver_assignment'),
    path('delivery-status/', views.delivery_status_view, name='delivery_status'),
    path('payment-management/', views.payment_management_view, name='payment_management'),
    path('invoice-management/', views.invoice_management_view, name='invoice_management'),
    path('pod-management/', views.pod_management_view, name='pod_management'),
]

