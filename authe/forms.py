
from django import forms

class SignIn(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)

class ForgotPassword(forms.Form):
	email = forms.EmailField(max_length=100)