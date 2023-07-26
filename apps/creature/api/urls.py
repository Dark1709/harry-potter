from django.urls import path
from . import views

urlpatterns = [
    path('Creature', views.CreatureAPIView.as_view(), name='creature-list'),
    path('Creature/<int:pk>', views.CreatureAPIView.as_view(), name='creature-detail'),
]