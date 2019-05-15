from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

# Create your views here.
class snippet_List(generics.ListCreateAPIView):
    # 이 클래스가 가질 queryset과 serializer 미리 선언
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user);

class snippet_Detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
