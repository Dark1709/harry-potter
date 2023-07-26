from django.urls import path
from . import views

urlpatterns = [
    path('Location', views.LocationAPIView.as_view(), name='location-list'),
    path('Location/<int:pk>', views.LocationAPIView.as_view(), name='location-detail'),
]