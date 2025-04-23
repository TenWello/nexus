# from unittest import TestCase
#
# from django.urls import reverse
#
# from category.models import Category
#
#
# class CategoryTests(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(name='Elektronika', slug='elektronika', is_main=True)
#
#     def test_category_list_template_content(self):
#         response = self.client.get(reverse('category-list'))
#         self.assertEqual(response, "Elektronika")