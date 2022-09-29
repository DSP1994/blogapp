from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Blog
from .forms import CommentForm


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 3


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
                'new_comment': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blog = post
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            'blog_details.html',
            {
                'post': post,
                'comments': comments,
                'new_comment': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )
