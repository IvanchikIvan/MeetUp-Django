"""
URL configuration for spacealien project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name='home'),
    path('history/', views.history_view, name='history'),
    path('places/', views.places_view, name='places'),
    path('preferences/', views.preferences_view, name='preferences'),
    path('preferences/change/', views.change_preferences),
    path('meet/<str:meet_id>/', views.meet_view, name='meet'),
    path("create/meet/", views.create_meet),
    path('account/', views.account_view, name='account'),
    path('account/login/', views.login_user, name='login'),
    path('account/logout/', views.logout_user, name='logout'),
    path('account/register/', views.register_user, name='register'),
    path('fakefastapi/', views.fakefastapi, name='fakefastapi'),
    path('meet/<str:meet_id>/remove_user/<int:user_id>/', views.remove_user_from_meet, name='remove_user_from_meet'),
]

handler404 = 'main.views.handle_404'
