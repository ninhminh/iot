from django.urls import path
from .views import LoginView, GetAllUsersView, SensorDataListView, ContronlPump,LatestSensorDataView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', GetAllUsersView.as_view(), name='get_all_users'),
    path('data/', SensorDataListView.as_view(), name='data_list'),
    path('control_pump/', ContronlPump.as_view(), name='control_pump'),
    path('lastData/', LatestSensorDataView.as_view()),
]
