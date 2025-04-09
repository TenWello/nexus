from django.test import TestCase
from category.forms import RegionForm
from category.models import Region


class RegionFormTest(TestCase):
    def test_region_invalid_form_data(self):
        form_data = {
            'name': '',
        }
        form = RegionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)