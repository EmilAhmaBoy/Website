from django.shortcuts import render, redirect, reverse
from .forms import UserSignup
from django.contrib.auth import authenticate, login, logout

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
  if request.method == 'GET':
    form = UserSignup()
    context = {
      'form': form
    }
    return render(request, 'pages/signup.html', context)
  elif request.method == 'POST':
    form = UserSignup(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      username = request.POST['username']
      password = request.POST['password1']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
      return redirect(reverse('forum'))
    else:
      context = {
        'form': form
      }
      return render(request, 'pages/signup.html', context)

