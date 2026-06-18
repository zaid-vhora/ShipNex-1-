from django.db import models
from app_modules.userapp.models import CustomUser

# ========== TRANSPORTER PROFILE MODEL ==========
class TransporterProfile(models.Model):
    """Transporter profile and information"""
    REGISTRATION_STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('suspended', 'Suspended'),
    ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='transporter_profile')
    company_name = models.CharField(max_length=100)
    company_registration_number = models.CharField(max_length=50, unique=True)
    license_number = models.CharField(max_length=50)
    business_license = models.FileField(upload_to='licenses/')
    
    # Contact
    office_address = models.TextField()
    office_phone = models.CharField(max_length=15)
    office_email = models.EmailField()
    
    # Details
    year_established = models.IntegerField()
    number_of_vehicles = models.IntegerField()
    coverage_area = models.TextField(help_text="Coverage cities/states")
    
    # Status
    registration_status = models.CharField(max_length=20, choices=REGISTRATION_STATUS, default='pending')
    is_verified = models.BooleanField(default=False)
    rating = models.FloatField(default=5.0, help_text="1-5 rating")
    total_deliveries = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'transporter_profile'
        verbose_name = 'Transporter Profile'
        verbose_name_plural = 'Transporter Profiles'
    
    def __str__(self):
        return self.company_name


# ========== TRANSPORTER VEHICLE MODEL ==========
class TransporterVehicle(models.Model):
    """Vehicles owned by transporter"""
    VEHICLE_STATUS = [
        ('active', 'Active'),
        ('maintenance', 'Under Maintenance'),
        ('inactive', 'Inactive'),
    ]
    
    transporter = models.ForeignKey(TransporterProfile, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=50)
    capacity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Capacity in kg")
    
    # Details
    registration_number = models.CharField(max_length=50)
    insurance_number = models.CharField(max_length=50)
    pollution_certificate = models.CharField(max_length=50)
    
    # Status
    status = models.CharField(max_length=20, choices=VEHICLE_STATUS, default='active')
    last_service_date = models.DateField(null=True, blank=True)
    next_service_date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'transporter_vehicle'
        verbose_name = 'Transporter Vehicle'
        verbose_name_plural = 'Transporter Vehicles'
    
    def __str__(self):
        return f"{self.vehicle_number} - {self.transporter.company_name}"


# ========== SHIPMENT ASSIGNMENT MODEL ==========
class ShipmentAssignment(models.Model):
    """Assignment of shipments to transporter"""
    ASSIGNMENT_STATUS = [
        ('assigned', 'Assigned'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ]
    
    shipment = models.ForeignKey('userapp.Shipment', on_delete=models.CASCADE, related_name='assignments')
    transporter = models.ForeignKey(TransporterProfile, on_delete=models.CASCADE, related_name='assignments')
    vehicle = models.ForeignKey(TransporterVehicle, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Assignment Details
    status = models.CharField(max_length=20, choices=ASSIGNMENT_STATUS, default='assigned')
    assigned_date = models.DateTimeField(auto_now_add=True)
    accepted_date = models.DateTimeField(null=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    
    # Cost
    assignment_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Notes
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'transporter_assignment'
        verbose_name = 'Shipment Assignment'
        verbose_name_plural = 'Shipment Assignments'
        ordering = ['-assigned_date']
    
    def __str__(self):
        return f"{self.shipment.tracking_number} → {self.transporter.company_name}"


# ========== EARNINGS MODEL ==========
class Earnings(models.Model):
    """Earnings for transporter"""
    transporter = models.ForeignKey(TransporterProfile, on_delete=models.CASCADE, related_name='earnings')
    assignment = models.ForeignKey(ShipmentAssignment, on_delete=models.CASCADE, related_name='earnings')
    
    # Amount
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Platform commission")
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Dates
    earned_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    
    is_paid = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'transporter_earnings'
        verbose_name = 'Earnings'
        verbose_name_plural = 'Earnings'
        ordering = ['-earned_date']
    
    def __str__(self):
        return f"{self.transporter.company_name} - {self.net_amount}"
