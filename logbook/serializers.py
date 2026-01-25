from rest_framework import serializers
from .models import Trip, LogbookEntry, Media

class MediaSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ['id', 'entry', 'file', 'file_url', 'media_type', 'uploaded_at']
        read_only_fields = ['uploaded_at']

    def get_file_url(self, obj):
        try:
            return obj.file.url
        except:
            return None

class LogbookEntrySerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = LogbookEntry
        fields = ['id', 'trip', 'timestamp', 'latitude', 'longitude', 'sog', 'cog', 'notes', 'media', 'created_at']
        read_only_fields = ['created_at']

class TripSerializer(serializers.ModelSerializer):
    entries = LogbookEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'name', 'start_date', 'end_date', 'status', 'entries', 'created_at']
        read_only_fields = ['created_at']
