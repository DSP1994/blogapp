from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Blog


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 4


class BlogDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            'blog_details.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked
            },
        )
    