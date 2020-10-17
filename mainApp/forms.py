from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput
from usersApp.models import *


class TagsForm(forms.Form):
    name = forms.CharField(label='name', required=False)