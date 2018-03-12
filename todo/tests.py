from django.test import TestCase
from todo.views import get_index
from django.core.urlresolvers import resolve

class SecondHomePageTest(TestCase):
    def test2_home_page_resolves(self):
        home_page2 = resolve('/todo/')
        self.assertEqual(home_page2.func, get_index)
        
        
        
        