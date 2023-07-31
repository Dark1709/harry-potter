from django.urls import path
from . import views

urlpatterns = [
    path('animal', views.AnimalAPIView.as_view(), name='animal-list'),
    path('animal/<int:pk>', views.AnimalAPIView.as_view(), name='animal-detail')
]