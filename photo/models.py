from django.db import models
from album.models import Album

class Photo(models.Model):
    title = models.CharField(max_length=250, blank=False, name="title")
    subtitle = models.CharField(max_length=250, blank=True, name="subtitle")
    description = models.TextField(max_length=1000, blank=True, name="description")
    publication_date = models.DateField(auto_created=False, name="publication_date")
    created_at = models.DateTimeField(auto_now_add=True, name="created_at")
    updated_at = models.DateTimeField(auto_now=True, name="updated_at")
    image_url = models.ImageField(upload_to='photos', blank=False, name="image_url")
    album = models.ForeignKey(Album, null=True, blank=True, name="album", related_name='photos', on_delete=models.SET_NULL)
    is_thumbnail = models.BooleanField(default=False, name="is_thumbnail")

    def __str__(self):
        return self.title