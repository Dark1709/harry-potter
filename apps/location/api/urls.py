from django.urls import path
from . import views

urlpatterns = [
    path('location', views.LocationAPIView.as_view(), name='location-list'),
    path('location/<int:pk>', views.LocationAPIView.as_view(), name='location-detail'),
]