from django.shortcuts import render

# ========== USER APP VIEWS ==========
# Homepage and public pages views

def index_view(request):
    return render(request, 'tmp_user/index.html')


def login_view(request):
    return render(request, 'tmp_user/login.html')


def register_view(request):
    return render(request, 'tmp_user/register.html')


def tracking_view(request):
    return render(request, 'tmp_user/tracking.html')


def about_view(request):
    return render(request, 'tmp_user/about.html')


def services_view(request):
    return render(request, 'tmp_user/services.html')


def contact_view(request):
    return render(request, 'tmp_user/contact.html')
