from django.shortcuts import render
from accounts.forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form}

    if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            newUser = User.objects.create_user(email=email, password=password)

    return render(request, 'auth/register.html', context)