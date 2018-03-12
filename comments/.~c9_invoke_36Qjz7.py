from django.test import TestCase
from comments.views import *
from django.core.urlresolvers import resolve

class CommentsPageTest(TestCase):
    def comments_page_resolves(self):
        comments_page = resolve('/chat/')
        self.assertEqual(c.func, get_index)
        
        
        
        