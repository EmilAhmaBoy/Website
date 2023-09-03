from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'pages/index.html')

def info(request):
  return render(request, 'pages/info.html')

def forum(request):
  return render(request, 'pages/forum.html')

def signin(request):
  return render(request, 'pages/signin.html')

def signup(request):
  return render(request, 'pages/signup.html')

