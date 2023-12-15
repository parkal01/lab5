from django.urls import path
from .views import PublicPostList

urlpatterns = [
    path('api/public/', PublicPostList.as_view(), name='public_posts'),
   
]