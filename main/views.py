import json

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseBadRequest
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

from main import error
from .models import Meet, User, History, UserProfile


def home_view(request):
    """Render the home page template"""
    context = {}
    if request.user.is_authenticated:
        meets = Meet.objects.filter(users=request.user)
        context["meets"] = meets
    return render(request, "index.html", context=context)


def dialog(request):
    """Render dialog"""
    return render(request, "dialog_template.html")


def register_user(request):
    """Handle user registration"""
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=email).exists():
            return render(request, "register.html", {
                          "error": "Username already exists"})

        user = User.objects.create_user(
            username=email, email=email, password=password,
            first_name=first_name, last_name=last_name
        )
        user_profile = UserProfile(
            user=user
        )
        user_profile.save()

        return redirect("login")

    return render(request, "register.html")


def login_user(request):
    """Handle user login"""
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, "login.html", {
                          "error": "Неверный email или пароль"})

        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            # Extract the 'next' parameter from the URL
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect("home")
        return render(request, "login.html", {
                      "error": "Invalid login credentials"})

    return render(request, "login.html")


@login_required(login_url="/account/login/")
def account_view(request):
    user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'info': user_profile.get_info()
    }
    return render(request, "account.html", context=context)


def history_view(request):
    """Render history page"""
    context = {}
    if request.user.is_authenticated:
        history = History.objects.filter(user=request.user)
        context["history"] = history

    return render(request, "history.html", context=context)


def places_view(request):
    """Render places page"""
    return render(request, "places.html")


@login_required(login_url="/account/login/")
def preferences_view(request):
    """Render preferences page"""
    return render(request, "preferences.html")


@login_required(login_url="/account/login/")
def meet_view(request, meet_id):
    """Render meet page"""
    context = {}
    try:
        if request.method == "POST":
            if 'features' in request.POST:
                cuisines = request.POST.getlist('cuisines')
                features = request.POST.getlist('features')
                context = {
                    'features': features,
                    'cuisines': cuisines
                }
                print(context)
                return render(request, 'test.html', context=context)
            elif 'email' in request.POST:
                email = request.POST['email']
                meet = Meet.objects.get(id=meet_id)
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    return HttpResponseBadRequest("Пользователь с указанной почтой не найден.")
                meet.users.add(user)
                meet.save()

                return JsonResponse({"status": "success"})
        else:
            context['meet_id'] = meet_id
            meet = Meet.objects.get(id=meet_id)
            context['meet'] = meet
            meets = Meet.objects.filter(users=request.user)
            context["meets"] = meets
            AllUsers = User.objects.all()
            participants = meet.users.all()
            
            with open("main/static/form_resources/features.json", "r", encoding="utf-8") as file:
                features = json.load(file)
            with open("main/static/form_resources/cuisine.json", "r", encoding="utf-8") as file:
                cuisine = json.load(file)

            context["features"] = features
            context["cuisines"] = cuisine
            context['users'] = AllUsers
            context['participants'] = participants
            
            return render(request, 'meet.html', context=context)
    except Exception as e:
        print(e)
        return HttpResponseBadRequest("Invalid request method")



def logout_user(request):
    """Handle user logout"""
    logout(request)
    return redirect("home")


def handle_404(request, exception):
    """Render a custom 404 template"""
    return render(request, "404.html")


@login_required(login_url="/account/login/")
def create_meet(request):
    """Create meet and return id meet"""
    if request.method == "POST":
        json_data_string = request.body.decode('utf-8')

        try:
            json_data = json.loads(json_data_string)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON format')
        try:
            creator = request.user
            meet = Meet.objects.create(
                name=json_data['meet_name'],
                creator=creator
            )
            meet.users.set([creator])
        except error.DatabaseError:
            return redirect("home")
        except error.CriticalError:
            return redirect("home")
        except Exception:
            return redirect("home")

        return JsonResponse({'meet_id': meet.id})
    else:
        return HttpResponseBadRequest("Invalid request method")


def change_preferences(request):
    """Change the user preferences"""
    if request.method == "POST":
        message = request.POST.get("message")
        print(f"Received message: {message}")
        return HttpResponse("Message received successfully!")

    return HttpResponseBadRequest("Invalid request method")


def fakefastapi(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)
            return JsonResponse({'status': 'success', 'data': data})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


@login_required(login_url="/account/login/")
def remove_user_from_meet(request, meet_id, user_id):
    try:
        meet = Meet.objects.get(id=meet_id)
        user = User.objects.get(id=user_id)
        meet.users.remove(user)
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})