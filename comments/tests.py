from django.test import TestCase
from comments.views import get_index
from django.core.urlresolvers import resolve

class CommentsPageTest(TestCase):
    def comments_page_resolves(self):
        comments_page = resolve('/chat/')
        self.assertEqual(comments_page.func, get_index)
        
        
        
        