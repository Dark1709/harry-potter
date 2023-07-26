from django.urls import path
from . import views

urlpatterns = [
    path('Characters', views.CharacterAPIView.as_view(), name='character-list'),
    path('Characters/<int:pk>', views.CharacterAPIView.as_view(), name='character-detail'),
]