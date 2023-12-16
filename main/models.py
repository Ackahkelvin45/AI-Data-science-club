from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255, null=True)
    cotent = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)
    writer = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="blog/")

    

class Events(models.Model):
    title = models.CharField(max_length=255, null=True)
    about = models.TextField(null=True)
    date = models.DateTimeField(null=True)
    image = models.ImageField(null=True, blank=True, upload_to="events/")