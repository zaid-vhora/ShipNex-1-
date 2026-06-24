from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from app_modules.userapp.models import Shipment
import datetime
import random

User = get_user_model()

# ========== USER APP VIEWS ===========
# Homepage and public pages views

def index_view(request):
    return render(request, 'tmp_user/index.html')


def login_view(request):
    context = {}
    if request.method == 'POST':
        credential = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        target_role = request.POST.get('target_role', '').strip()

        user = authenticate(request, username=credential, password=password)
        if user is None and credential:
            try:
                user_by_email = User.objects.get(email__iexact=credential)
                user = authenticate(request, username=user_by_email.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            if target_role and user.role != target_role:
                context['login_error'] = 'This account does not have access to the requested dashboard.'
            else:
                login(request, user)
                if user.role == 'transporter':
                    return redirect('/transportapp/index_view/')
                if user.role == 'admin':
                    return redirect('/adminapp/index_view/')
                if user.role == 'logistics':
                    return redirect('/logisticsapp/')
                return redirect('/userapp/dashboard/')  # Redirect customer to their dashboard
        else:
            context['login_error'] = 'Invalid email or password. Please try again.'

    return render(request, 'tmp_user/login.html', context)


def register_view(request):
    context = {
        'roles': [
            ('customer', 'Customer'),
            ('transporter', 'Transporter'),
            ('logistics', 'Logistics'),
            ('admin', 'Admin'),
        ]
    }

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        role = request.POST.get('role', 'customer')
        terms = request.POST.get('terms')

        if not terms:
            context['register_error'] = 'You must agree to the Terms of Service and Privacy Policy.'
        elif password != confirm_password:
            context['register_error'] = 'Passwords do not match.'
        elif not email or not password:
            context['register_error'] = 'Please provide an email and password.'
        elif User.objects.filter(email__iexact=email).exists():
            context['register_error'] = 'This email is already registered.'
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.role = role
            if role == 'admin':
                user.is_staff = True
            user.save()
            return redirect('login')

    return render(request, 'tmp_user/register.html', context)


def tracking_view(request):
    return render(request, 'tmp_user/tracking.html')


def about_view(request):
    return render(request, 'tmp_user/about.html')


def services_view(request):
    return render(request, 'tmp_user/services.html')


def contact_view(request):
    return render(request, 'tmp_user/contact.html')


# ========== REGISTERED CUSTOMER DASHBOARD & APIS ==========

@login_required
def dashboard_view(request):
    # Fetch shipments for current logged-in customer
    shipments = Shipment.objects.filter(user=request.user)
    
    # Calculate stats
    total_bookings = shipments.count()
    pending_pickups = shipments.filter(status='pending').count()
    in_transit = shipments.filter(status='in_transit').count()
    delivered = shipments.filter(status='delivered').count()
    cancelled = shipments.filter(status='cancelled').count()
    
    context = {
        'shipments': shipments,
        'total_bookings': total_bookings,
        'pending_pickups': pending_pickups,
        'in_transit': in_transit,
        'delivered': delivered,
        'cancelled': cancelled,
        # Prepopulate sender info
        'sender_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
        'sender_email': request.user.email,
        'sender_phone': request.user.phone or '',
        'sender_address': request.user.address or '',
    }
    return render(request, 'tmp_user/dashboard.html', context)


@login_required
@require_POST
def create_shipment_view(request):
    try:
        sender_name = request.POST.get('sender_name', '').strip()
        sender_email = request.POST.get('sender_email', '').strip()
        sender_phone = request.POST.get('sender_phone', '').strip()
        sender_address = request.POST.get('sender_address', '').strip()
        
        receiver_name = request.POST.get('receiver_name', '').strip()
        receiver_email = request.POST.get('receiver_email', '').strip()
        receiver_phone = request.POST.get('receiver_phone', '').strip()
        receiver_address = request.POST.get('receiver_address', '').strip()
        
        shipment_type = request.POST.get('shipment_type', 'standard')
        weight = float(request.POST.get('weight', 0) or 0)
        dimensions = request.POST.get('dimensions', '').strip()
        description = request.POST.get('description', '').strip()
        
        if not sender_name or not sender_address or not receiver_name or not receiver_address:
            return JsonResponse({'success': False, 'message': 'Sender and receiver name and address are required.'}, status=400)
        
        if weight <= 0:
            return JsonResponse({'success': False, 'message': 'Weight must be greater than 0 kg.'}, status=400)

        # Cost Calculation
        cost_rates = {
            'standard': (100.0, 150.0),
            'express': (250.0, 350.0),
            'overnight': (500.0, 600.0),
            'freight': (80.0, 1000.0)
        }
        
        rate, min_charge = cost_rates.get(shipment_type, (100.0, 150.0))
        computed_cost = max(weight * rate, min_charge)
        
        # Generate tracking number
        date_str = datetime.date.today().strftime('%Y%m%d')
        random_str = ''.join(random.choices('0123456789', k=6))
        tracking_number = f"SHP-{date_str}-{random_str}"
        
        while Shipment.objects.filter(tracking_number=tracking_number).exists():
            random_str = ''.join(random.choices('0123456789', k=6))
            tracking_number = f"SHP-{date_str}-{random_str}"
            
        shipment = Shipment.objects.create(
            tracking_number=tracking_number,
            user=request.user,
            sender_name=sender_name,
            sender_email=sender_email,
            sender_phone=sender_phone,
            sender_address=sender_address,
            receiver_name=receiver_name,
            receiver_email=receiver_email,
            receiver_phone=receiver_phone,
            receiver_address=receiver_address,
            shipment_type=shipment_type,
            weight=weight,
            dimensions=dimensions,
            description=description,
            cost=computed_cost,
            status='pending'
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Shipment booked successfully!',
            'tracking_number': shipment.tracking_number,
            'cost': float(shipment.cost)
        })
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error booking shipment: {str(e)}'}, status=500)


@login_required
@require_POST
def cancel_shipment_view(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id, user=request.user)
    if shipment.status in ['draft', 'pending']:
        shipment.status = 'cancelled'
        shipment.save()
        return JsonResponse({'success': True, 'message': 'Shipment cancelled successfully.'})
    else:
        return JsonResponse({
            'success': False, 
            'message': f'Cannot cancel shipment with status: {shipment.get_status_display()}. It might already be processed or delivered.'
        }, status=400)


def track_shipment_json(request, tracking_number):
    try:
        shipment = Shipment.objects.get(tracking_number=tracking_number)
        
        status_steps = [
            ('pending', 'Shipment Booked', 'Order placed and confirmed', shipment.created_at),
            ('confirmed', 'Confirmed', 'Logistics hub confirmed booking', None),
            ('picked_up', 'Picked Up', 'Collected from sender location', None),
            ('in_transit', 'In Transit', 'Out for delivery via express route', None),
            ('out_for_delivery', 'Out For Delivery', 'Package is out with delivery executive', None),
            ('delivered', 'Delivered', 'Package successfully hand-delivered', shipment.delivery_date)
        ]
        
        status_seq = ['pending', 'confirmed', 'picked_up', 'in_transit', 'out_for_delivery', 'delivered']
        
        current_status = shipment.status
        if current_status == 'cancelled':
            timeline = [
                {
                    'title': 'Shipment Booked',
                    'desc': 'Order placed and confirmed',
                    'date': shipment.created_at.strftime('%b %d, %H:%M') if shipment.created_at else '',
                    'completed': True,
                    'current': False
                },
                {
                    'title': 'Shipment Cancelled',
                    'desc': 'Booking was cancelled by the sender/system',
                    'date': shipment.updated_at.strftime('%b %d, %H:%M') if shipment.updated_at else '',
                    'completed': True,
                    'current': True,
                    'cancelled': True
                }
            ]
        else:
            try:
                curr_idx = status_seq.index(current_status)
            except ValueError:
                curr_idx = 0
                
            timeline = []
            for i, (val, title, desc, dt) in enumerate(status_steps):
                completed = i <= curr_idx
                current = i == curr_idx
                
                date_str = ''
                if completed:
                    if dt:
                        date_str = dt.strftime('%b %d, %H:%M')
                    else:
                        offset_hours = i * 4
                        date_val = shipment.created_at + datetime.timedelta(hours=offset_hours)
                        date_str = date_val.strftime('%b %d, %H:%M')
                else:
                    date_str = 'Pending'
                    
                timeline.append({
                    'title': title,
                    'desc': desc,
                    'date': date_str,
                    'completed': completed,
                    'current': current
                })
        
        return JsonResponse({
            'success': True,
            'tracking_number': shipment.tracking_number,
            'status': shipment.get_status_display(),
            'status_raw': shipment.status,
            'sender_name': shipment.sender_name,
            'sender_city': shipment.sender_address.split(',')[-1].strip() if ',' in shipment.sender_address else shipment.sender_address,
            'receiver_name': shipment.receiver_name,
            'receiver_city': shipment.receiver_address.split(',')[-1].strip() if ',' in shipment.receiver_address else shipment.receiver_address,
            'shipment_type': shipment.get_shipment_type_display(),
            'weight': f"{shipment.weight} kg",
            'dimensions': shipment.dimensions or 'N/A',
            'cost': f"₹{shipment.cost:.2f}",
            'timeline': timeline
        })
    except Shipment.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Tracking ID not found.'}, status=404)


def logout_view(request):
    logout(request)
    return redirect('home')
