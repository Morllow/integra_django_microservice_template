from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=128, required=True,
                             help_text='yours@email.com')

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
