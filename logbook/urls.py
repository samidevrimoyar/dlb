from rest_framework.routers import DefaultRouter
from .views import TripViewSet, LogbookEntryViewSet, MediaViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet, basename='trip')
router.register(r'entries', LogbookEntryViewSet, basename='entry')
router.register(r'media', MediaViewSet, basename='media')

urlpatterns = router.urls
