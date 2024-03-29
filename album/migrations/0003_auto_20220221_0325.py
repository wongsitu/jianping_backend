# -*- coding: utf-8 -*-
# Generated by Django 4.0.2 on 2022-02-21 03:25
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def slugify_title(apps, schema_editor):
    '''
    We can't import the Album model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    Album = apps.get_model('album', 'Album')
    for album in Album.objects.all():
        album.slug = slugify(album.title)
        album.save()


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_album_slug'),
    ]

    operations = [
        migrations.RunPython(slugify_title),
    ]
