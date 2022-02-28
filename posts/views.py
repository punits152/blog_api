from django.shortcuts import render


from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

from django.contrib.auth import get_user_model

from rest_framework import viewsets

# Create your views here.



class PostList(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated,]
    #queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        set = [post for post in Post.objects.all() if post.author==self.request.user]
        return set



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

"""
OLD Way of creating redundent views for list and detail
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
"""

# We can use a viewset with the router in urls file

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



