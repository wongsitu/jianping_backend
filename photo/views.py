from photo.models import Photo
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from photo.serializers import PhotoSerializer

class Photo(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_thumbnail']