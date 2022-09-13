
from photo.models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Photo
        fields = ['id', 'title', 'title_en', 'title_cn', 'subtitle', 'subtitle_en', 'subtitle_cn', 
                'description', 'description_en', 'description_cn', 'publication_date', 'created_at', 
                'updated_at', 'image_url', 'album', 'is_thumbnail']