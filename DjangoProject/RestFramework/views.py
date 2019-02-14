from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions


# Create your views here.
# viewsets -> get,post등에 대한 함수를 하나하나 만들 필요 X but,세세한 지정이 불가능

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
