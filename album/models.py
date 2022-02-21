from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=250, blank=False)
    subtitle = models.CharField(max_length=250, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title