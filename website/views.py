from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import registrationForm
from .models import Record



def index(request):
    records = Record.objects.all()
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
        return render(request, 'index.html', {'records' : records})


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged Out successfully')
    return redirect('index')

def registerUser(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)

            login(request, user)
            messages.success(request, 'Successfully Registered. Welcome '+username)
            return redirect('index')
    
    else:
        form = registrationForm()
        return render(request, 'register.html', {'form' : form})
    
    return render(request, 'register.html', {'form' : form})


def customerRecord(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record' : record})
    
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('index')