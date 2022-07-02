from re import T
from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth import get_user_model

class Link(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    target_url =  models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank = True, unique = True)
    author = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='links_link')
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default= True)


