from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet


class TweetDetailView(DetailView):
    template_name = 'detail_view.html'

    def get_object(self, queryset=Tweet.objects.all()):
        print (self.kwargs)
        #kwargs so that we can access al keyword arguments can pk or the id
        pk = self.kwargs['pk']
        print (pk)
        return Tweet.objects.get(id=pk)
        #id becomes pk instead of 1 (assigned value only)

class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = 'list_view.html'
