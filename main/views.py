from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def home_view(request):
    """Render the home page template"""
    return render(request, 'index.html')


def dialog(request):
    """Render dialog"""
    return render(request, 'dialog_template.html')


def register_user(request):
    """Handle user registration"""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        else:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')


def login_user(request):
    """Handle user login"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Неверный email или пароль'})
            
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


def history_view(request):
    """Render history page"""
    return redirect('home')


def meet_view(request, id):
    """Render meet page"""
    return redirect('home')


def logout_user(request):
    """Handle user logout"""
    logout(request)
    return redirect('home')


def handle_404(request, exception):
    """Render a custom 404 template"""
    return render(request, "404.html")



def create_meet(request):
    return render(request, 'meet.html')
