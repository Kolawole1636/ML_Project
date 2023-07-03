
from django.urls import path
from . import views

urlpatterns = [
    path('diabetes_home', views.diabetes_home, name="diabetes_home"),
    
]
