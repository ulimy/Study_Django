from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.
class snippet_List(generics.ListCreateAPIView):
    # 이 클래스가 가질 queryset과 serializer 미리 선언
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # generic이 알아서 보냄 따로 적어줄 필요 X

class snippet_Detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
