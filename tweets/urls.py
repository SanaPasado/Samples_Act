
from django.urls import path
from .views import *

urlpatterns = [
    path('', TweetListView.as_view(), name='list_view'),
    path('1/', TweetDetailView.as_view(), name='detail_view'),
]