from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from photo import views as PhotoViews
from album import views as AlbumViews

router = routers.DefaultRouter()
router.register(r'photos', PhotoViews.Photo)
router.register(r'albums', AlbumViews.Album)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
