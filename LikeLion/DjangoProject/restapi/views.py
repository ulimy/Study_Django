from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.http import QueryDict
from .forms import PostForm
from .models import Post

# Create your views here.

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        rs = Post.objects.all()
        data = [{'pk':post.pk, 'message':post.message} for post in rs]
        return JsonResponse(data,safe=False)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponse(status=201)
        data = form.errors
        return JsonResponse(data,status=400)


@csrf_exempt
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'GET':
        return JsonResponse({'pk':post.pk, 'message':post.message})

    elif request.method == 'PUT':
        put = QueryDict(request.body)
        form = PostForm(put,instance=post)
        if form.is_valid():
            post=form.save();
            data = {'pk': post.pk , 'message': post.message}
            return JsonResponse(data=data,status=201)
        return JsonResponse(form.errors)

    elif request.method == 'DELETE':
        post.delete();
        return HttpResponse('',status=204)
