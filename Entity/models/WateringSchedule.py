from django.db import models
from .SensorData import SensorData
class WateringSchedule(models.Model):
    device = models.ForeignKey(SensorData, on_delete=models.CASCADE, related_name='watering_schedules')
    start_time = models.TimeField()
    end_time = models.TimeField()
    frequency = models.CharField(max_length=50)  # e.g., "Daily", "Weekly"
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)