from .views import Login, Main
from django.urls import path

urlpatterns = [
    path('LogIn', Login.as_view()),
    path('Main',Main.as_view()),
]