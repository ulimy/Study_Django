from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    # query set
    blogs = Blog.objects
    return render (request,'blog/home.html',{'blogs' : blogs})

def detail(request,blog_pk):
    blog_detail = get_object_or_404(Blog,pk=blog_pk)
    return render(request,'blog/detail.html',{'blog' : blog_detail})
