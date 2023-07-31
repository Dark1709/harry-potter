from django.urls import path
from . import views

urlpatterns = [
    path('spell', views.SpellAPIView.as_view(), name='spell-list'),
    path('spell/<int:pk>', views.SpellAPIView.as_view(), name='spell-detail'),
]