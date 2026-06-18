from django.contrib.auth import authenticate, get_user_model, login
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import VehicleForm, DriverForm, WarehouseForm, PaymentForm
from .models import Vehicle, Driver, Warehouse, Payment

User = get_user_model()

# Create your views here.
def index_view(request):
    total_vehicles = Vehicle.objects.count()
    total_drivers = Driver.objects.count()
    total_warehouses = Warehouse.objects.count()
    total_payments = Payment.objects.count()
    return render(request, 'tmp_admin/index1.html', {
        'total_vehicles': total_vehicles,
        'total_drivers': total_drivers,
        'total_warehouses': total_warehouses,
        'total_payments': total_payments,
    })

def deliveries_view(request):
    return render(request,'tmp_admin/deliveries.html')

def login_view(request):
    context = {}
    if request.method == 'POST':
        credential = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=credential, password=password)
        if user is None and credential:
            try:
                user_by_email = User.objects.get(email__iexact=credential)
                user = authenticate(request, username=user_by_email.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            if user.role != 'admin':
                context['error'] = 'You do not have admin access for this login.'
            else:
                login(request, user)
                return redirect('/adminapp/index_view/')
        else:
            context['error'] = 'Invalid username or password.'

    return render(request, 'tmp_admin/login.html', context)


def vehicles_view(request):
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '')
    vehicles = Vehicle.objects.all()
    if q:
        vehicles = vehicles.filter(Q(vehicle_number__icontains=q) | Q(driver_name__icontains=q))
    if status == 'active':
        vehicles = vehicles.filter(is_active=True)
    elif status == 'inactive':
        vehicles = vehicles.filter(is_active=False)

    return render(request, 'tmp_admin/vehicles.html', {
        'vehicles': vehicles,
        'search_query': q,
        'status_filter': status,
        'total_vehicles': Vehicle.objects.count(),
        'active_vehicles': Vehicle.objects.filter(is_active=True).count(),
        'inactive_vehicles': Vehicle.objects.filter(is_active=False).count(),
    })


def vehicle_add(request):
    form = VehicleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('vehicles_view')
    return render(request, 'tmp_admin/admin_form.html', {
        'form': form,
        'title': 'Add Vehicle',
        'subtitle': 'Create new fleet vehicle records for your admin panel',
        'submit_label': 'Create Vehicle',
        'cancel_url': '/adminapp/vehicles_view/',
    })


def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('vehicles_view')
    return render(request, 'tmp_admin/admin_form.html', {
        'form': form,
        'title': 'Edit Vehicle',
        'subtitle': f'Update vehicle {vehicle.vehicle_number}',
        'submit_label': 'Save Changes',
        'cancel_url': '/adminapp/vehicles_view/',
    })


def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
    return redirect('vehicles_view')


def drivers_view(request):
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '')
    drivers = Driver.objects.select_related('vehicle').all()
    if q:
        drivers = drivers.filter(Q(name__icontains=q) | Q(phone__icontains=q) | Q(license_number__icontains=q))
    if status == 'active':
        drivers = drivers.filter(is_active=True)
    elif status == 'inactive':
        drivers = drivers.filter(is_active=False)

    return render(request, 'tmp_admin/drivers.html', {
        'drivers': drivers,
        'search_query': q,
        'status_filter': status,
        'total_drivers': Driver.objects.count(),
        'active_drivers': Driver.objects.filter(is_active=True).count(),
        'inactive_drivers': Driver.objects.filter(is_active=False).count(),
    })


def driver_add(request):
    form = DriverForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('drivers_view')
    return render(request, 'tmp_admin/admin_form.html', {
        'form': form,
        'title': 'Add Driver',
        'subtitle': 'Create a new driver record and assign a vehicle if needed',
        'submit_label': 'Create Driver',
        'cancel_url': '/adminapp/drivers_view/',
    })


def driver_edit(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    form = DriverForm(request.POST or None, instance=driver)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('drivers_view')
    return render(request, 'tmp_admin/admin_form.html', {
        'form': form,
        'title': 'Edit Driver',
        'subtitle': f'Update driver {driver.name}',
        'submit_label': 'Save Changes',
        'cancel_url': '/adminapp/drivers_view/',
    })


def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        driver.delete()
    return redirect('drivers_view')


def warehouses_view(request):
    q = request.GET.get('q', '').strip()
    warehouses = Warehouse.objects.all()
    if q:
        warehouses = warehouses.filter(Q(name__icontains=q) | Q(city__icontains=q) | Q(manager_name__icontains=q))
    return render(request, 'tmp_admin/warehouses.html', {
        'warehouses': warehouses,
        'search_query': q,
        'total_warehouses': warehouses.count(),
    })


def warehouse_add(request):
    form = WarehouseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('warehouses_view')
    return render(request, 'tmp_admin/admin_form.html', {
        'form': form,
        'title': 'Add Warehouse',
        'subtitle': 'Create a warehouse record with capacity and manager details',
        'submit_label': 'Create Warehouse',
        'cancel_url': '/adminapp/warehouses_view/',
    })


def warehouse_edit(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    form = WarehouseForm(request.POST or None, instance=warehouse)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('warehouses_view')
    return render(request, 'tmp_admin/admin_form.html', {
        'form': form,
        'title': 'Edit Warehouse',
        'subtitle': f'Update warehouse {warehouse.name}',
        'submit_label': 'Save Changes',
        'cancel_url': '/adminapp/warehouses_view/',
    })


def warehouse_delete(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        warehouse.delete()
    return redirect('warehouses_view')


def payments_view(request):
    q = request.GET.get('q', '').strip()
    payments = Payment.objects.all()
    if q:
        payments = payments.filter(Q(transaction_id__icontains=q) | Q(reference_number__icontains=q))
    return render(request, 'tmp_admin/payments.html', {
        'payments': payments,
        'search_query': q,
        'total_payments': payments.count(),
    })

def payment_add(request):
    form = PaymentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('payments_view')
    return render(request, 'tmp_admin/admin_form.html', {
        'form': form,
        'title': 'Add Payment',
        'subtitle': 'Create and track payment records for shipments',
        'submit_label': 'Create Payment',
        'cancel_url': '/adminapp/payments_view/',
    })


def payment_edit(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    form = PaymentForm(request.POST or None, instance=payment)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('payments_view')
    return render(request, 'tmp_admin/admin_form.html', {
        'form': form,
        'title': 'Edit Payment',
        'subtitle': f'Update payment {payment.transaction_id}',
        'submit_label': 'Save Changes',
        'cancel_url': '/adminapp/payments_view/',
    })


def payment_delete(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        payment.delete()
    return redirect('payments_view')


def reports_view(request):
    return render(request,'tmp_admin/reports.html')

def settings_view(request):
    return render(request,'tmp_admin/settings.html')

def shipments_view(request):
    return render(request,'tmp_admin/shipments.html')

def transporters_view(request):
    return render(request,'tmp_admin/transporters.html')

def users_view(request):
    return render(request,'tmp_admin/users.html')

