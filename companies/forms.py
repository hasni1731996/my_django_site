#-*- coding: utf-8 -*-
from django import forms
class SignupForm(forms.Form):
   # django gives a number of predefined fields
   # CharField and EmailField are only two of them
   # go through the official docs for more field details
   name = forms.CharField(label='Enter your name', max_length=100)
   email = forms.EmailField(label='Enter your email', max_length=100)
   password = forms.CharField(label='Enter your passowrd', max_length=100,widget = forms.PasswordInput())

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField()

class Cookies_form(forms.Form):
   name = forms.CharField(max_length = 100)

class BootstrapForm_(forms.Form):
   name = forms.CharField(label='Enter your name', max_length=100)
   email = forms.EmailField(label='Enter your email', max_length=100)
   password = forms.CharField(label='Enter your passowrd', max_length=100,widget = forms.PasswordInput())