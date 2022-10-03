from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from blog.views import BlogList, BlogDetail, BlogLike


class TestUrls(TestCase):
    """ Test to see if the urls are loading properly """

    def test_blog_page_status_code(self):
        """ Test to see if the blog page loads correctly """
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details_status_code(self):
        """ Test to see if the blog details page loads correctly """
        url = reverse('blog_details', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, BlogDetail)

    def test_blog_liked_status_code(self):
        """ Test to see if the 'when blog is liked' page loads correctly """
        url = reverse('blog_like', args=['some-slug-2'])
        self.assertEqual(resolve(url).func.view_class, BlogLike)
