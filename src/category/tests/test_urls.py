from django.test import TestCase
from django.urls import reverse


class RegionUrlTest(TestCase):
    def test_region_url(self):
        url= reverse('region')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'region.html')