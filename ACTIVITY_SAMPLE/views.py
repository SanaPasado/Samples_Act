from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')

def contact_page(request):
    if request.method == 'POST':
            print(request.POST)#.get('full_name')
        #you can alter get or just remove it to get what model elements you want
    return render(request, 'contact/contact.html')
