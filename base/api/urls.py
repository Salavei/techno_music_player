from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import SongViewSet

router = SimpleRouter()
router.register(r'song', SongViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls))
]