from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Blog, Comment


class BlogTest(TestCase):
    """ Testing a Blog """
    def create_blog(
        self,
        title='test',
        content='hello there!',
        author=User.objects.create_author(
            username.self.username,
        ),
    ):

        return Blog.objects.create(
            title=title,
            content=content,
            created_on=timezone.now(),
            author=author
            )

    def test_blog_creation(self):
        test = self.create_blog()
        
        self.assertTrue(isinstance(test, Blog))
        self.assertEqual(test.__str__(), test.title)
    