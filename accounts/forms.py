from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "First Name"}))

    last_name = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               "placeholder": "Last Name"}))


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