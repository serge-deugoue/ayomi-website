from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2', ]


class ChangeUserDataForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={
                'id': 'form-email',
                'required': True,
                'placeholder': 'ex: test@test.com'
            }),
            'first_name': forms.TextInput(attrs={
                'id': 'form-firstName',
                'required': True,
                'placeholder': 'ex: Paul'
            }),
            'last_name': forms.TextInput(attrs={
                'id': 'form-lastName',
                'required': True,
                'placeholder': 'ex: Delorme'
            }),
        }
