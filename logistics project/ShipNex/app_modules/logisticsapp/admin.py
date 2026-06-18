from django.contrib import admin
from .models import Delivery, Route, Invoice

# ========== DELIVERY ADMIN ==========
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'delivery_date', 'status', 'delivered_by', 'signature_required')
    list_filter = ('status', 'delivery_date', 'signature_required', 'created_at')
    search_fields = ('shipment__tracking_number', 'delivery_address', 'delivered_by')
    readonly_fields = ('created_at', 'updated_at', 'proof_of_delivery')
    
    fieldsets = (
        ('Shipment', {
            'fields': ('shipment',)
        }),
        ('Delivery Schedule', {
            'fields': ('delivery_date', 'delivery_time_slot', 'delivery_address')
        }),
        ('Delivery Status', {
            'fields': ('status', 'delivered_by', 'signature_required')
        }),
        ('Special Instructions', {
            'fields': ('special_instructions', 'delivery_notes')
        }),
        ('Proof', {
            'fields': ('proof_of_delivery',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-delivery_date',)


# ========== ROUTE ADMIN ==========
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'source_city', 'destination_city', 'distance', 'estimated_time', 'cost', 'is_active')
    list_filter = ('is_active', 'source_city', 'destination_city', 'created_at')
    search_fields = ('name', 'source_city', 'destination_city')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Route Information', {
            'fields': ('name', 'is_active')
        }),
        ('Route Details', {
            'fields': ('source_city', 'destination_city', 'distance', 'estimated_time', 'cost')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('source_city', 'destination_city')


# ========== INVOICE ADMIN ==========
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'shipment', 'total', 'status', 'issue_date', 'due_date')
    list_filter = ('status', 'issue_date', 'due_date', 'created_at')
    search_fields = ('invoice_number', 'shipment__tracking_number')
    readonly_fields = ('created_at', 'updated_at', 'issue_date')
    
    fieldsets = (
        ('Invoice Information', {
            'fields': ('invoice_number', 'shipment', 'issue_date', 'due_date')
        }),
        ('Amount Details', {
            'fields': ('subtotal', 'tax', 'discount', 'total')
        }),
        ('Status', {
            'fields': ('status', 'paid_date')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-issue_date',)
