from django.db import models

# Create your models here.
class TodoItem(models.Model):
    name = models.CharField(max_length=30, blank=False)
    gone = models.BooleanField(blank=False, default=False)
    
def __str__(self):
    return self.name 