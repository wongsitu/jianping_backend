from django.db import models
from album.models import Album

class Photo(models.Model):
    title = models.CharField(max_length=250, blank=False, name="title")
    title_en = models.CharField(max_length=250, blank=True, name="title_en")
    title_cn = models.CharField(max_length=250, blank=True, name="title_cn")
    subtitle = models.CharField(max_length=250, blank=True, name="subtitle")
    subtitle_en = models.CharField(max_length=250, blank=True, name="subtitle_en")
    subtitle_cn = models.CharField(max_length=250, blank=True, name="subtitle_cn")
    description = models.TextField(max_length=1000, blank=True, name="description")
    description_en = models.TextField(max_length=1000, blank=True, name="description_en")
    description_cn = models.TextField(max_length=1000, blank=True, name="description_cn")
    publication_date = models.DateField(auto_created=False, name="publication_date")
    created_at = models.DateTimeField(auto_now_add=True, name="created_at")
    updated_at = models.DateTimeField(auto_now=True, name="updated_at")
    image_url = models.ImageField(upload_to='photos', blank=False, name="image_url")
    album = models.ForeignKey(Album, null=True, blank=True, name="album", related_name='photos', on_delete=models.SET_NULL)
    is_thumbnail = models.BooleanField(default=False, name="is_thumbnail")

    def __str__(self):
        print(self.title)
        return self.title