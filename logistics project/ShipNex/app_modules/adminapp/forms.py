from django import forms
from .models import Vehicle, Driver, Warehouse, Payment

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_number',
            'vehicle_type',
            'driver_name',
            'driver_phone',
            'capacity',
            'last_service',
            'is_active',
        ]
        widgets = {
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control-custom', 'style': 'text-transform:uppercase;'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control-custom'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'driver_phone': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control-custom', 'step': '0.01'}),
            'last_service': forms.DateInput(attrs={'class': 'form-control-custom', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            'name',
            'phone',
            'email',
            'license_number',
            'license_expiry',
            'license_status',
            'address',
            'date_of_birth',
            'vehicle',
            'is_active',
            'rating',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'phone': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control-custom'}),
            'license_number': forms.TextInput(attrs={'class': 'form-control-custom', 'style': 'text-transform:uppercase;'}),
            'license_expiry': forms.DateInput(attrs={'class': 'form-control-custom', 'type': 'date'}),
            'license_status': forms.Select(attrs={'class': 'form-control-custom'}),
            'address': forms.Textarea(attrs={'class': 'form-control-custom', 'rows': 3}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control-custom', 'type': 'date'}),
            'vehicle': forms.Select(attrs={'class': 'form-control-custom'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control-custom', 'step': '0.1', 'min': '1', 'max': '5'}),
        }

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = [
            'name',
            'city',
            'state',
            'country',
            'postal_code',
            'address',
            'capacity',
            'manager_name',
            'manager_phone',
            'is_active',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'city': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'state': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'country': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'address': forms.Textarea(attrs={'class': 'form-control-custom', 'rows': 3}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control-custom'}),
            'manager_name': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'manager_phone': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'transaction_id',
            'amount',
            'payment_method',
            'payment_status',
            'reference_number',
            'completed_date',
            'notes',
        ]

        widgets = {
            'transaction_id': forms.TextInput(attrs={'class': 'form-control-custom', 'style': 'text-transform:uppercase;'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control-custom', 'step': '0.01'}),
            'payment_method': forms.Select(attrs={'class': 'form-control-custom'}),
            'payment_status': forms.Select(attrs={'class': 'form-control-custom'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'completed_date': forms.DateTimeInput(attrs={'class': 'form-control-custom', 'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'class': 'form-control-custom', 'rows': 3}),
        }
