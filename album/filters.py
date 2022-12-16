from django_filters import rest_framework
from album.models import Album

class AlbumFilter(rest_framework.FilterSet):
    slug = rest_framework.CharFilter(field_name='slug', lookup_expr='iexact')