from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Shipment

# ========== CUSTOM USER ADMIN ==========
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'role', 'is_verified', 'is_staff')
    list_filter = ('role', 'is_verified', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('username', 'email', 'phone', 'first_name', 'last_name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Additional Info', {
            'fields': ('address', 'city', 'state', 'country', 'postal_code')
        }),
        ('Profile', {
            'fields': ('profile_picture', 'role', 'is_verified')
        }),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
    ordering = ('-created_at',)


# ========== SHIPMENT ADMIN ==========
@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'user', 'receiver_name', 'weight', 'status', 'cost', 'created_at')
    list_filter = ('status', 'shipment_type', 'created_at', 'delivery_date')
    search_fields = ('tracking_number', 'sender_name', 'receiver_name', 'sender_email', 'receiver_email')
    readonly_fields = ('tracking_number', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Shipment ID', {
            'fields': ('tracking_number', 'user')
        }),
        ('Sender Information', {
            'fields': ('sender_name', 'sender_email', 'sender_phone', 'sender_address')
        }),
        ('Receiver Information', {
            'fields': ('receiver_name', 'receiver_email', 'receiver_phone', 'receiver_address')
        }),
        ('Package Details', {
            'fields': ('shipment_type', 'weight', 'dimensions', 'description')
        }),
        ('Pricing & Status', {
            'fields': ('cost', 'status')
        }),
        ('Dates', {
            'fields': ('pickup_date', 'delivery_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-created_at',)
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('user',)
        return self.readonly_fields
