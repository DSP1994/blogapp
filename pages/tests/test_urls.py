from django.test import TestCase
from django.urls import reverse, resolve
from pages.views import contact, about, frontpage


class TestUrls(TestCase):
    """ Test to see if the urls are loading properly """

    def test_blog_url_is_resolved(self):
        """ Test to see if the home page loads correctly """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    
    def test_blog_url_is_resolved(self):
        """ Test to see if the contact me page loads correctly """
        response = self.client.get('contact/')
        self.assertEqual(response.status_code, 301)
    
    def test_blog_url_is_resolved(self):
        """ Test to see if the about section page loads correctly """
        response = self.client.get('about/')
        self.assertEqual(response.status_code, 404)

