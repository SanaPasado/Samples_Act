from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "username"}))

    email = forms.EmailField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "email"}))

    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               "placeholder": "password"}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               "placeholder": "Confirm Password"}))

    def clean_username(self):
        username = self.cleaned_data['username']
        foo = User.objects.filter(username=username)
        if foo.exists():
            raise forms.ValidationError('Username already exists')
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        foo = User.objects.filter(email=email)
        if foo.exists():
            raise forms.ValidationError('Email already exists')
        return email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords do not match')
        return data


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "fullname"}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               "placeholder": "Email"} ))


    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control',
               "placeholder": "Message"}))


    def clean(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Please enter a Gmail address")
        return email
    #this will check if gmail is contained in email, if not will make u enter a gmail address