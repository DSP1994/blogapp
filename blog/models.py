from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
from autoslug import AutoSlugField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(
        populate_from='title',
        max_length=200,
        unique=True,
        name='slug',
        editable=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author')
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('open_post', kwargs={'slug': str(self.slug)})

    def save(self, *args, **kwargs):
        self.slug = slugify(kwargs.pop('slug', self.slug))
        super().save(*args, **kwargs)


class Comment(models.Model):

    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
