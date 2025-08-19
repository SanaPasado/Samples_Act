
from jobs.models import Job

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView
from tweets.mixins import FormUserMixin
from tweets.forms import TweetModelForm


# Create your views here.
def job_detail_view(request, id=1):
    obj = Job.objects.get(id=id)
    print(obj)
    context = {
        'object' : obj,
    #     assigning html element to python element
    }
    return render(request, 'detail_view.html' , context )

def job_list_view(request):
    qs = Job.objects.all()
    print(qs)
    context = {
        'query' : qs,
    }
    return render(request, 'list_view.html' , context )



class JobDeleteView(DeleteView):
    model = Job
    template_name = 'delete_view.html'
    login_url = '/admin/login/'

class JobUpdateView(LoginRequiredMixin, FormUserMixin, UpdateView):
    template_name = 'update_view.html'
    queryset = Job.objects.all()
    login_url = '/admin/login/'






