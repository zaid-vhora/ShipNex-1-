from django.db import models
from django.utils import timezone

class Vehicle(models.Model):
    
    VEHICLE_TYPES = [
        ('bike', 'Motorcycle'),
        ('car', 'Car'),
        ('van', 'Van'),
        ('truck', 'Truck'),
        ('container', 'Container Truck'),
    ]
    
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    driver_name = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=15, blank=True)
    capacity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Capacity in kg")
    registration_date = models.DateField(auto_now_add=True)
    last_service = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'admin_vehicle'
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.vehicle_number} - {self.get_vehicle_type_display()}"



class Driver(models.Model):
    LICENSE_STATUS = [
        ('valid', 'Valid'),
        ('expired', 'Expired'),
        ('suspended', 'Suspended'),
    ]
    
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True)
    license_number = models.CharField(max_length=50, unique=True)
    license_expiry = models.DateField()
    license_status = models.CharField(max_length=20, choices=LICENSE_STATUS, default='valid')
    address = models.TextField()
    date_of_birth = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    rating = models.FloatField(default=5.0, help_text="1-5 rating")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'admin_driver'
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.license_number})"



class Warehouse(models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    address = models.TextField()
    capacity = models.IntegerField(help_text="Capacity in units")
    manager_name = models.CharField(max_length=100)
    manager_phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'admin_warehouse'
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'
        ordering = ['city', 'country']
    
    def __str__(self):
        return f"{self.name} - {self.city}, {self.country}"



class Payment(models.Model):

    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('upi', 'UPI'),
        ('wallet', 'Wallet'),
    ]
    
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    reference_number = models.CharField(max_length=100, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'admin_payment'
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"{self.transaction_id} - {self.amount}"