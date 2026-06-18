from django.contrib import admin
from .models import TransporterProfile, TransporterVehicle, ShipmentAssignment, Earnings

# ========== TRANSPORTER PROFILE ADMIN ==========
@admin.register(TransporterProfile)
class TransporterProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'registration_status', 'is_verified', 'rating', 'total_deliveries')
    list_filter = ('registration_status', 'is_verified', 'created_at')
    search_fields = ('company_name', 'company_registration_number', 'office_email', 'user__username')
    readonly_fields = ('created_at', 'updated_at', 'total_deliveries', 'rating')
    
    fieldsets = (
        ('User Account', {
            'fields': ('user',)
        }),
        ('Company Information', {
            'fields': ('company_name', 'company_registration_number', 'year_established')
        }),
        ('Licensing', {
            'fields': ('license_number', 'business_license')
        }),
        ('Contact Information', {
            'fields': ('office_address', 'office_phone', 'office_email')
        }),
        ('Operations', {
            'fields': ('number_of_vehicles', 'coverage_area')
        }),
        ('Verification & Status', {
            'fields': ('registration_status', 'is_verified', 'rating', 'total_deliveries')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-created_at',)


# ========== TRANSPORTER VEHICLE ADMIN ==========
@admin.register(TransporterVehicle)
class TransporterVehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'transporter', 'vehicle_type', 'capacity', 'status')
    list_filter = ('status', 'vehicle_type', 'created_at')
    search_fields = ('vehicle_number', 'registration_number', 'transporter__company_name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Vehicle Information', {
            'fields': ('transporter', 'vehicle_number', 'vehicle_type', 'capacity')
        }),
        ('Documentation', {
            'fields': ('registration_number', 'insurance_number', 'pollution_certificate')
        }),
        ('Maintenance', {
            'fields': ('last_service_date', 'next_service_date')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-created_at',)


# ========== SHIPMENT ASSIGNMENT ADMIN ==========
@admin.register(ShipmentAssignment)
class ShipmentAssignmentAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'transporter', 'vehicle', 'status', 'assigned_date', 'assignment_cost')
    list_filter = ('status', 'assigned_date', 'created_at')
    search_fields = ('shipment__tracking_number', 'transporter__company_name', 'vehicle__vehicle_number')
    readonly_fields = ('created_at', 'updated_at', 'assigned_date')
    
    fieldsets = (
        ('Assignment Details', {
            'fields': ('shipment', 'transporter', 'vehicle')
        }),
        ('Status & Dates', {
            'fields': ('status', 'assigned_date', 'accepted_date', 'completed_date')
        }),
        ('Cost', {
            'fields': ('assignment_cost',)
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-assigned_date',)


# ========== EARNINGS ADMIN ==========
@admin.register(Earnings)
class EarningsAdmin(admin.ModelAdmin):
    list_display = ('transporter', 'assignment', 'gross_amount', 'commission', 'net_amount', 'is_paid', 'payment_date')
    list_filter = ('is_paid', 'earned_date', 'payment_date', 'created_at')
    search_fields = ('transporter__company_name', 'assignment__shipment__tracking_number')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Transporter Information', {
            'fields': ('transporter', 'assignment')
        }),
        ('Amount Breakdown', {
            'fields': ('gross_amount', 'commission', 'net_amount')
        }),
        ('Payment Status', {
            'fields': ('is_paid', 'earned_date', 'payment_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-earned_date',)
