from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import BlogList, BlogDetail, BlogLike


class TestUrls(TestCase):
    """ Test to see if the urls are loading properly """

    def test_blog_url_is_resolved(self):
        """ Test to see if the blog page loads correctly """
        response = self.client.get('blog/')
        self.assertEqual(response.status_code, 200)
    
    def test_blog_url_is_resolved(self):
        """ Test to see if the blog details page loads correctly """
        response = self.client.get('<slug:slug>/')
        self.assertEqual(response.status_code, 301)
    
    def test_blog_url_is_resolved(self):
        """ Test to see if the 'when blog is liked' page loads correctly """
        response = self.client.get('like<slug:slug>')
        self.assertEqual(response.status_code, 404)

