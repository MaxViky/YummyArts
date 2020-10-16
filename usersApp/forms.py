from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput
from .models import *


class loginForm(forms.Form):
    username = forms.CharField(label='Nickname', required=False)
    password = forms.CharField(label='Password', required=False, widget=PasswordInput())


class regForms(forms.ModelForm):
    password1 = forms.CharField(label='Password', required=False, widget=PasswordInput())
    password2 = forms.CharField(label='Repeat the password', required=False, widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['name', 'post', 'tag']
