from django.urls import path
from . import views

urlpatterns = [
    path('Object', views.ObjectAPIView.as_view(), name='object-list'),
    path('Object/<int:pk>', views.ObjectAPIView.as_view(), name='object-detail'),
]