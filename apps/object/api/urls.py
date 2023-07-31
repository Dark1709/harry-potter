from django.urls import path
from . import views

urlpatterns = [
    path('object', views.ObjectAPIView.as_view(), name='object-list'),
    path('object/<int:pk>', views.ObjectAPIView.as_view(), name='object-detail'),
]