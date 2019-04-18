from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='Enter your name',max_length=100,required=True)
    password = forms.CharField(label='Enter your password',max_length=100, required=True)