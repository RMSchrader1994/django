from django.test import TestCase
from .models import *


class TodoItemTest(TestCase):
    def test_str_work(self):
        item = TodoItem()
        item.name = "Test Subject"
        self.assertEqual("Test Subject", str(item.name))