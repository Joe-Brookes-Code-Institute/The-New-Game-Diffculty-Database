from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title