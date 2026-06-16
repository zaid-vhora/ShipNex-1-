from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'tmp_admin/index1.html')

def deliveries_view(request):
    return render(request,'tmp_admin/deliveries.html')

def drivers_view(request):
    return render(request,'tmp_admin/drivers.html')

def login_view(request):
    return render(request,'tmp_admin/login.html')

def payments_view(request):
    return render(request,'tmp_admin/payments.html')

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

def vehicles_view(request):
    return render(request,'tmp_admin/vehicles.html')

def warehouses_view(request):
    return render(request,'tmp_admin/warehouses.html')