from django.shortcuts import render
from django.views import generic
from .models import Blog


class BlogList(generic.ListView):
    model = Blog
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 4
