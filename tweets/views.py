from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet

class TweetDetailView(DetailView):
    template_name = 'detail_view.html'

    def get_object(self, queryset=Tweet.objects.all()):
        return Tweet.objects.get(id=1)

class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = 'list_view.html'
