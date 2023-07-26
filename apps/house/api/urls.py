from django.urls import path
from . import views

urlpatterns = [
    path('Houses', views.HouseAPIView.as_view(), name='house-list'),
    path('Houses/<int:pk>', views.HouseAPIView.as_view(), name='house-detail'),
]