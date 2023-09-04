from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSignup(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
  
  username = forms.CharField(label='Никнейм', min_length=3, max_length=24, required=True,
                            widget=forms.TextInput(attrs={}))
  email = forms.CharField(label='Электронная почта', min_length=7, max_length=52, required=True,
                            widget=forms.TextInput(attrs={}))
  first_name = forms.CharField(label='Имя', min_length=0, max_length=24, required=False,
                            widget=forms.TextInput(attrs={}))
  last_name = forms.CharField(label='Фамилия', min_length=0, max_length=24, required=False,
                            widget=forms.TextInput(attrs={}))
  password1 = forms.CharField(label='Пароль', min_length=8, max_length=32, required=True,
                            widget=forms.PasswordInput(attrs={}))
  password2 = forms.CharField(label='Подтверждение пароля', min_length=0, max_length=32,
                            required=True, widget=forms.PasswordInput(attrs={}))