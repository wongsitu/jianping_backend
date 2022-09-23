
from photo.models import Photo
from album.models import Album
from rest_framework import serializers
from django.core import serializers as core_serializers


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    # album = serializers.SerializerMethodField()

    def get_album(self, photo):
        album = Album.objects.get(pk=photo.album.id)
        serialized_album = core_serializers.serialize('json', list(album), fields=('description','description_cn', 'description_en', 'subtitle'))
        return serialized_album

    class Meta:
        model = Photo
        fields = ['id', 'title', 'title_en', 'title_cn', 'subtitle', 'subtitle_en', 'subtitle_cn', 
                'description', 'description_en', 'description_cn', 'publication_date', 'created_at', 
                'updated_at', 'image_url', 'is_thumbnail']