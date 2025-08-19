
from django.shortcuts import render

from ACTIVITY_SAMPLE.forms import ContactForm, RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

def home_page(request):
    return render(request, 'home.html')

def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form,
    }
    return render(request, "contact/contact.html", context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form}

    if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            newUser = User.objects.create_user(username=username, email=email, password=password)

    return render(request, 'auth/register.html', context)