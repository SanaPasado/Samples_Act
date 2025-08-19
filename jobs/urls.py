
from django.urls import path, re_path
from .views import *

app_name = 'jobs'
urlpatterns = [
    path('', job_list_view, name='list_view'),
    path('<int:pk>/', job_detail_view, name='detail_view'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='delete_view'),
]