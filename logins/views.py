from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from WebLab.views import Index, profile


def LogIn(request):
    if request.user.is_authenticated:
        return redirect(profile)

    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            data = f.cleaned_data
            uname = data['username']
            pword = data['password']

            u = authenticate(username=uname, password=pword)
            if u is not None:
                login(request, u)
                return redirect(Index)
            else:
                f.add_error(None, 'wrong username and/or password')
                return render(request, 'logins/login.html', {'f': f, 'user': request.user})
    return render(request, 'logins/login.html', {'f': LoginForm(), 'user': request.user})



def Register(request):
    if request.user.is_authenticated:
        return redirect(profile)
    if request.method == 'POST':
        f = RegForm(request.POST)
        if f.is_valid():
            data = f.cleaned_data
            u = User.objects.create_user(username=data['username'], password=data['pword'], email=data['email'])
            u.first_name = data['first_name']
            u.last_name = data['last_name']
            u.save()
            login(request, u)
            return redirect(profile)
        else:
            return render(request, 'logins/register.html', {'f': f, 'user': request.user})
    return render(request, 'logins/register.html', {'f': RegForm(), 'user': request.user})


def LogOut(request):
    logout(request)
    return redirect(Index)