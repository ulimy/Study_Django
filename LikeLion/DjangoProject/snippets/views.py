from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.
class snippet_List(APIView):

    def get(self,request,formant=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.error,status=HTTP_400_BAD_REQUEST)


class snippet_Detail(APIView):

    # pk로 snippet 가져오는 함수 만들어놓고 가져다 쓰기
    def get_object(self,pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,pk,format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=HTTP_204_NO_CONTENT)
