from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse

def blog(request):
    blog = Blog.objects.all()
    return HttpResponse(blog)