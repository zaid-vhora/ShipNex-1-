from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect

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
                return redirect('/userapp/index/')
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
