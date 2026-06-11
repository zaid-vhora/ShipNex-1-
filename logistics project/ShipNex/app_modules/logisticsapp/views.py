from django.shortcuts import render

# Create your views here.
def logistics_Dashboard_view(request):
    return render(request, 'tmp_logistics/logistics_Dashboard.html')

def Shipment_Management_view(request):
    return render(request, 'tmp_logistics/shipment_management.html')


def shipment_tracking_view(request):
    return render(request, 'tmp_logistics/shipment_tracking.html')


def vehicle_assignment_view(request):
    return render(request, 'tmp_logistics/vehicle_assignment.html')


def driver_assignment_view(request):
    return render(request, 'tmp_logistics/driver_assignment.html')


def delivery_status_view(request):
    return render(request, 'tmp_logistics/delivery_status.html')


def payment_management_view(request):
    return render(request, 'tmp_logistics/payment_management.html')


def invoice_management_view(request):
    return render(request, 'tmp_logistics/invoice_management.html')


def pod_management_view(request):
    return render(request, 'tmp_logistics/pod.html')