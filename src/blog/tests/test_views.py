from django.test import TestCase
from django.urls import reverse
from blog.models import Blog



class BlogViewTest(TestCase):
    def test_create_blog(self):
        self.url = reverse('blog')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('blogs', response.context)
        self.assertEqual(len(response.context['blogs']), 0)
        self.assertTemplateUsed(response, 'blog.html')


