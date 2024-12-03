from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from Entity.models.SensorData import SensorData
from Entity.models.User import User  
from .serializers import UserSerializer, SensorDataSerializer

from django.http import JsonResponse
from mqtt_config.mqtt_client import client
import json

class LoginView(APIView):
    def post(self, request):
        if 'email' not in request.data:
            return Response({"massage":"Vui lòng nhập tên tài khoản"}, status=400)
        email = request.data['email']
        if 'password' not in request.data:
            return Response({"password":"Vui lòng nhập mật khẩu"}, status=400)
        password = request.data['password']
        try:
            user = User.objects.get(Email = email, Password = password)
        except:
            return Response({"massage":"Sai tài khoản"}, status=401)
        return Response({"ID":user.id}, status=201)

class GetAllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        print(serializer.data) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class SensorDataView(APIView):
    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LatestSensorDataView(APIView):
    def get(self, request, *args, **kwargs):
        # Lấy dữ liệu cảm biến có timestamp gần nhất
        latest_sensor_data = SensorData.objects.latest('timestamp')
        serializer = SensorDataSerializer(latest_sensor_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SensorDataListView(APIView):
    def get(self, request):
        sensorData = SensorData.objects.all()
        serializer = SensorDataSerializer(sensorData, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContronlPump(APIView):
    # API để điều khiển bơm
    def get(self,request):
        # Lấy trạng thái bơm từ query params
        pump_state = request.GET.get("state")
        
        if pump_state is None:
            return JsonResponse({"error": "State parameter missing"}, status=400)

        # Chuyển đổi trạng thái thành boolean
        pump_state = pump_state.lower() == "on"
        
        # Gửi thông điệp MQTT để điều khiển bơm
        payload = json.dumps({"pumpState": pump_state})
        client.publish("iot/system", payload)
        
        return JsonResponse({"status": "success", "pumpState": pump_state})