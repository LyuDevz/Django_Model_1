from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.http import HttpResponse

def home(request):
    # Blog에 있는 모든 객체들을 가져오는 것
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})