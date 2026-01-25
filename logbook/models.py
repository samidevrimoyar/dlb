from django.db import models
from django.conf import settings

class Trip(models.Model):
    STATUS_CHOICES = (
        ('PLANNED', 'Planned'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trips')
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.status})"

class LogbookEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='entries')
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True, blank=True, related_name='entries')
    timestamp = models.DateTimeField()
    
    # Validation uses standard WGS84 range
    latitude = models.DecimalField(max_digits=9, decimal_places=6) # -90 to +90
    longitude = models.DecimalField(max_digits=9, decimal_places=6) # -180 to +180
    
    sog = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Speed Over Ground (knots)")
    cog = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True, help_text="Course Over Ground (degrees)")
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Logbook Entries"

    def __str__(self):
        return f"{self.timestamp} - {self.latitude},{self.longitude}"

class Media(models.Model):
    MEDIA_TYPES = (
        ('IMAGE', 'Image'),
        ('VIDEO', 'Video'),
    )
    entry = models.ForeignKey(LogbookEntry, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='logbook_media/%Y/%m/%d/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='IMAGE')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media for {self.entry}"
