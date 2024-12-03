from django.db import models
class MQTTLog(models.Model):
    topic = models.CharField(max_length=255)
    payload = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)