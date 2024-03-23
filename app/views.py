from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def create_meet(request):
    return render(request, 'meet.html')