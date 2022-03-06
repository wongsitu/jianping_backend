from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from photo import views as PhotoViews
from album import views as AlbumViews
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'photos', PhotoViews.Photo)
router.register(r'albums', AlbumViews.Album)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)