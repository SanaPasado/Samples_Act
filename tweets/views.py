from django.shortcuts import render
from .models import Tweet

def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    print(obj)
    context = {
        'object' : obj,
    #     assigning html element to python element
    }
    return render(request, 'detail_view.html' , context )

def tweet_list_view(request):
    qs = Tweet.objects.all()
    print(qs)
    context = {
        'query' : qs,
    }
    return render(request, 'list_view.html' , context )
