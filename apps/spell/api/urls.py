from django.urls import path
from . import views

urlpatterns = [
    path('Spell', views.SpellAPIView.as_view(), name='spell-list'),
    path('Spell/<int:pk>', views.SpellAPIView.as_view(), name='spell-detail'),
]