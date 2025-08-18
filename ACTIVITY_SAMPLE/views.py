from django.shortcuts import render

from ACTIVITY_SAMPLE.forms import ContactForm


def home_page(request):
    return render(request, 'home.html')

def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form,
    }
    return render(request, "contact/contact.html", context)
