from django.urls import path
from photo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('photos/', views.Photo.as_view())
]