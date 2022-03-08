from album.models import Album
from rest_framework import viewsets
from album.serializers import AlbumSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import Pagination

class Album(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = Pagination