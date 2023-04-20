from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Blog, Post
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User


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


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post.html'
    paginate_by = 3


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        template_name = 'open_post.html'
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

    def post(self, request, slug, *args, **kwargs):
        template_name = 'open_post.html'
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)


class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('blog')


class UpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
    field = ['title', 'image', 'content', 'status']


class DeleteView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')


class BlogLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Blog, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_details.html', args=[slug]))


class ProfilePage(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'profile.html'
