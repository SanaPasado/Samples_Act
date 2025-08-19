from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from .models import Tweet
from tweets.mixins import FormUserMixin
from tweets.forms import TweetModelForm


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

class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = 'delete_view.html'
    login_url = '/admin/login/'

class TweetUpdateView(LoginRequiredMixin, FormUserMixin, UpdateView):
    form_class = TweetModelForm
    template_name = 'update_view.html'
    queryset = Tweet.objects.all()
    login_url = '/admin/login/'

class TweetCreateView(LoginRequiredMixin, FormUserMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'create_view.html'
    login_url = '/admin/login/'


