from django.test import TestCase
from .views import *

class MVT(TestCase):
    def test_index_template(self):
        response = self.client.get('/todo/')
        self.assertTemplateUsed(response, "todo/index.html")
        
