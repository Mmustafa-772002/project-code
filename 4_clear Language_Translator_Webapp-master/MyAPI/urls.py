from django.urls import path, include
from . import views
from rest_framework import routers

from .views import save_file_on_server


urlpatterns = [
    path('', views.translated, name='home'),
    path('about/', views.about, name='about'),
    path('save_file_on_server/', save_file_on_server, name='save_file_on_server'),
]