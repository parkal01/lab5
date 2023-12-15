from rest_framework import generics
from .models import Post
from .serializer import PostSerializer

class PublicPostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
