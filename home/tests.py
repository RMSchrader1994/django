from django.test import TestCase
from home.views import *
from django.core.urlresolvers import resolve

class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def text_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home/base.html")
        self.assertTemplateUsed(response, "home/index.html")
        
        
        