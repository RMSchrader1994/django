from django.test import TestCase
from about.views import get_index
from django.core.urlresolvers import resolve

class AboutPageTest(TestCase):
    def about_page_resolves(self):
        about_page = resolve('/about/')
        self.assertEqual(about.func, get_index)
        
        
        
        