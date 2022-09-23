
from album.models import Album
from photo.models import Photo
from rest_framework import serializers
from photo.serializers import PhotoSerializer

class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    photos = serializers.SerializerMethodField()

    def get_photos(self, album):
        photos = Photo.objects.filter(is_thumbnail=True, album=album)
        serializer = PhotoSerializer(instance=photos, many=True)
        return serializer.data

    class Meta:
        model = Album
        fields = ['id', 'slug', 'title', 'title_en', 'title_cn', 
                'subtitle', 'subtitle_en', 'subtitle_cn', 'description', 'description_en', 'description_cn',
                'publication_date', 'created_at', 'updated_at', 'photos']