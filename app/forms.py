from django import forms
from . models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50)
class SignupForm(forms.Form):
    email = forms.EmailField()
    confpass= forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
# class SignupForm(forms.ModelForm):
#     confpass = forms.CharField(label="Confirm Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confpass = cleaned_data.get("confpass")
#
#         if password and confpass and password != confpass:
#             self.add_error('confpass', "Passwords do not match.")
#
#         if password:
#             if len(password) < 8:
#                 self.add_error('password', "Password must be at least 8 characters long.")
#             if not any(char.isdigit() for char in password):
#                 self.add_error('password', "Password must contain at least one digit.")
#             if not any(char.isalpha() for char in password):
#                 self.add_error('password', "Password must contain at least one letter.")
#
#         return cleaned_data
class ShopForm(forms.ModelForm):
    class Meta:
        model = shopsmodel
        fields = ['email', 'name', 'bio', 'location','locationlink', 'phone']
class offerForm(forms.ModelForm):
    class Meta:
        model = offermodel
        fields = ['name', 'description', 'photo']
class ShopSearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=False)