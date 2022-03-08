from django_filters import rest_framework
from album.models import Album

class PhotoFilter(rest_framework.FilterSet):
    slug = rest_framework.CharFilter(field_name='album__slug', lookup_expr='iexact')
    is_thumbnail = rest_framework.BooleanFilter(field_name='is_thumbnail')