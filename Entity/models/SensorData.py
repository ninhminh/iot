from django.db import models
from .User import User
class SensorData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices', null=True)
    temperature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    soil_moisture = models.IntegerField(null=True)
    water_level = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Data at {self.timestamp}: Temp: {self.temperature}, Humidity: {self.humidity}, Soil: {self.soil_moisture}, Water: {self.water_level}"