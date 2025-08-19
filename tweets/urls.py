
from django.urls import path, re_path
from .views import *

app_name = 'tweets'
urlpatterns = [
    path('', TweetListView.as_view(), name='list_view'),
    path('<int:pk>/', TweetDetailView.as_view(), name='detail_view'),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete_view'),
    path('<int:pk>/create/', TweetCreateView.as_view(), name='create_view'),
]