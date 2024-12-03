from django.apps import AppConfig
from django.utils.module_loading import import_string

class MqttConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mqtt_config'
    def ready(self):
        # Khi ứng dụng được khởi động, bắt đầu MQTT client
        from .mqtt_client import start_mqtt
        start_mqtt()
