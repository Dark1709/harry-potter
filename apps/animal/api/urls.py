from django.urls import path
from . import views

urlpatterns = [
    path('Animal', views.AnimalAPIView.as_view(), name='animal-list'),
    path('Animal/<int:pk>', views.AnimalAPIView.as_view(), name='animal-detail')
]