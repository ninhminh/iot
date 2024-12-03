from rest_framework import serializers
from Entity.models.User import User
from Entity.models.SensorData import SensorData
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'UserName', 'Email', 'FullName']

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature', 'humidity', 'soil_moisture', 'water_level', 'timestamp']