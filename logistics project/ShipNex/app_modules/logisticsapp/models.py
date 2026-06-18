from django.db import models
from app_modules.userapp.models import CustomUser

# ========== DELIVERY MODEL ==========
class Delivery(models.Model):
    """Delivery information"""
    DELIVERY_STATUS = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('rescheduled', 'Rescheduled'),
    ]
    
    shipment = models.OneToOneField('userapp.Shipment', on_delete=models.CASCADE, related_name='delivery')
    delivery_date = models.DateField()
    delivery_time_slot = models.CharField(max_length=50, help_text="e.g., 9AM-12PM")
    delivery_address = models.TextField()
    status = models.CharField(max_length=20, choices=DELIVERY_STATUS, default='scheduled')
    
    # Delivery Details
    delivered_by = models.CharField(max_length=100, blank=True)
    signature_required = models.BooleanField(default=False)
    proof_of_delivery = models.ImageField(upload_to='deliveries/', blank=True, null=True)
    
    # Notes
    special_instructions = models.TextField(blank=True)
    delivery_notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'logistics_delivery'
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'
    
    def __str__(self):
        return f"Delivery - {self.shipment.tracking_number}"


# ========== ROUTE MODEL ==========
class Route(models.Model):
    """Delivery routes"""
    name = models.CharField(max_length=100)
    source_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    distance = models.DecimalField(max_digits=8, decimal_places=2, help_text="Distance in km")
    estimated_time = models.IntegerField(help_text="Estimated time in hours")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'logistics_route'
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        unique_together = ['source_city', 'destination_city']
    
    def __str__(self):
        return f"{self.source_city} → {self.destination_city}"


# ========== INVOICE MODEL ==========
class Invoice(models.Model):
    """Invoice management"""
    INVOICE_STATUS = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]
    
    invoice_number = models.CharField(max_length=50, unique=True)
    shipment = models.ForeignKey('userapp.Shipment', on_delete=models.CASCADE, related_name='invoices')
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(max_length=20, choices=INVOICE_STATUS, default='draft')
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'logistics_invoice'
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        ordering = ['-issue_date']
    
    def __str__(self):
        return f"{self.invoice_number} - {self.shipment.tracking_number}"
