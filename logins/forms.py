from django import forms
from django.contrib.auth.models import User


class RegForm(forms.Form):
    first_name = forms.CharField(label = "First Name", max_length=120)
    last_name = forms.CharField(label = "Last Name", max_length=120)
    email = forms.CharField(label="Email", widget=forms.EmailInput)
    username = forms.CharField(label="UserName", max_length=120)
    pword = forms.CharField(label="Password", max_length=32, widget = forms.PasswordInput)
    pword_r = forms.CharField(label="Confirm Password", max_length=32, widget=forms.PasswordInput)

    def clean(self):
        pw = self.cleaned_data['pword']
        pwr = self.cleaned_data['pword_r']

        if pw != pwr:
            raise forms.ValidationError({'pword': ['Password mismatch',]})

        return self.cleaned_data

    def clean_username(self):
        uname = self.cleaned_data['username']
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError('Username already exist')
        return uname

class LoginForm(forms.Form):
    username = forms.CharField(label="UserName", max_length=120)
    password = forms.CharField(label="Password", max_length=32, widget=forms.PasswordInput)
    pass