from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

# def login(request):
#     return render(request, 'usuarios/login.html')