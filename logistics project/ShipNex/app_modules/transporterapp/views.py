from django.shortcuts import render

# Create your views here.
def assigned_view(request):
    return render(request, 'tmp_transporter/assigned_shipments.html')

def drivers_view(request):
    return render(request, 'tmp_transporter/drivers.html')

def earnings_view(request):
    return render(request, 'tmp_transporter/earnings.html')

def index_view(request):
    return render(request, 'tmp_transporter/index.html')

def pod_view(request):
    return render(request, 'tmp_transporter/pod.html')

def routes_view(request):
    return render(request, 'tmp_transporter/routes.html')

def settings_view(request):
    return render(request, 'tmp_transporter/settings.html')

def shipment_view(request):
    return render(request, 'tmp_transporter/shipment_details.html')

def vehicle_view(request):
    return render(request, 'tmp_transporter/vehicles.html')