
from album.models import Album
from rest_framework import serializers
from photo.serializers import PhotoSerializer


class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'subtitle', 'description', 'publication_date', 'created_at', 'updated_at', 'photos']