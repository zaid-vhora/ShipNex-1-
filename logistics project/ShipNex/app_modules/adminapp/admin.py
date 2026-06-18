from django.contrib import admin
from .models import Vehicle, Driver, Warehouse, Payment

# ========== VEHICLE ADMIN ==========
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'vehicle_type', 'driver_name', 'capacity', 'is_active', 'created_at')
    list_filter = ('vehicle_type', 'is_active', 'created_at')
    search_fields = ('vehicle_number', 'driver_name', 'driver_phone')
    readonly_fields = ('created_at', 'updated_at', 'registration_date')
    
    fieldsets = (
        ('Vehicle Information', {
            'fields': ('vehicle_number', 'vehicle_type', 'capacity')
        }),
        ('Driver Information', {
            'fields': ('driver_name', 'driver_phone')
        }),
        ('Service Details', {
            'fields': ('registration_date', 'last_service')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-created_at',)


# ========== DRIVER ADMIN ==========
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'license_status', 'phone', 'vehicle', 'rating', 'is_active')
    list_filter = ('license_status', 'is_active', 'created_at')
    search_fields = ('name', 'phone', 'email', 'license_number')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'date_of_birth', 'email', 'phone', 'address')
        }),
        ('License Details', {
            'fields': ('license_number', 'license_expiry', 'license_status')
        }),
        ('Assignment', {
            'fields': ('vehicle',)
        }),
        ('Performance', {
            'fields': ('rating', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-created_at',)


# ========== WAREHOUSE ADMIN ==========
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'manager_name', 'capacity', 'is_active')
    list_filter = ('country', 'city', 'is_active', 'created_at')
    search_fields = ('name', 'city', 'manager_name', 'manager_phone')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Warehouse Information', {
            'fields': ('name', 'capacity')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'country', 'postal_code')
        }),
        ('Manager Details', {
            'fields': ('manager_name', 'manager_phone')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('city', 'country')


# ========== PAYMENT ADMIN ==========
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'amount', 'payment_method', 'payment_status', 'payment_date')
    list_filter = ('payment_status', 'payment_method', 'payment_date')
    search_fields = ('transaction_id', 'reference_number')
    readonly_fields = ('created_at', 'updated_at', 'payment_date')
    
    fieldsets = (
        ('Transaction Information', {
            'fields': ('transaction_id', 'reference_number', 'amount')
        }),
        ('Payment Details', {
            'fields': ('payment_method', 'payment_status')
        }),
        ('Dates', {
            'fields': ('payment_date', 'completed_date')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-payment_date',)
