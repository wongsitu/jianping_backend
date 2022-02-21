
from photo.models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Photo
        fields = ['id', 'title', 'subtitle', 'description', 'publication_date', 'created_at', 'updated_at', 'image_url', 'album', 'is_thumbnail']