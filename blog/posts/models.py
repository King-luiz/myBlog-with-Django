from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(default= datetime.now)
    def __str__(self):
        return self.title
