from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import registrationForm, addRecordForm
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
    
def deleteRecord(request, pk):
    if request.user.is_authenticated:
        to_delete = Record.objects.get(id=pk)

        to_delete.delete()
        messages.success(request, f'Record For id {pk} deleted')
        return redirect('index')
    
    else:
        messages.error(request, 'You must be logged in to perform this action')
        return redirect('index')
    
def modifyRecord(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = addRecordForm(request.POST or None, instance=current_record)

        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully')
            return redirect('index')
        return render(request, 'modify.html', {'form' : form})
    else:
        messages.error(request, 'You need to log in to perform this action')
        return redirect('index')




def create(request):
    form = addRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record added successfully')
                return redirect('index')
        else:
            return render(request, 'create.html', {'form' : form})
    else:
        messages.error(request, 'You need to log in to perform this action')
        return redirect('index')