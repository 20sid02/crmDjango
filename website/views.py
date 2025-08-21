from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials. Try again')
            return redirect('index')

    else:
        return render(request, 'index.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged Out successfully')
    return redirect('index')

def registerUser(request):



    return render(request, 'register.html')