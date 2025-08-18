
from django.urls import path
from .views import *

urlpatterns = [
    path('', tweet_list_view, name='list_view'),
    path('1/', tweet_detail_view, name='detail_view'),
]