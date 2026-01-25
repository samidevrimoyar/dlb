from rest_framework import viewsets, permissions, parsers
from .models import Trip, LogbookEntry, Media
from .serializers import TripSerializer, LogbookEntrySerializer, MediaSerializer

class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LogbookEntryViewSet(viewsets.ModelViewSet):
    serializer_class = LogbookEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LogbookEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MediaViewSet(viewsets.ModelViewSet):
    serializer_class = MediaSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_queryset(self):
        return Media.objects.filter(entry__user=self.request.user)
