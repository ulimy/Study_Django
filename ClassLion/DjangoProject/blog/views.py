from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    # query set
    blogs = Blog.objects
    return render (request,'blog/home.html',{'blogs' : blogs})

def detail(request,blog_pk):
    blog_detail = get_object_or_404(Blog,pk=blog_pk)
    return render(request,'blog/detail.html',{'blog' : blog_detail})

def new(request):
    return render(request,'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return render(request,'blog/detail.html',{'blog' : blog})
