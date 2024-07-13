from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def loginer(request, form):
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')

    user = authenticate(username=username, password=password)
    return login(request, user)



def logoutt(request):
    logout(request)
    return HttpResponseRedirect("/")


def index(request):
    return render(request, 'login/index.html')



def loginuser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {"form":form})

def registeruser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'login/registration.html', {'form':form})

