from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class registrationForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email Address'}))

    firstName = forms.CharField(max_length = 64, label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First Name'}))

    lastName = forms.CharField(max_length = 64, label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'password', 'reppasword')
