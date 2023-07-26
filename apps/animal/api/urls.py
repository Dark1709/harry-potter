from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    'api/v1/Animal',
    views.AnimalModelViewSet,
    basename='animal'
)

urlpatterns = [
    path('Animal', views.AnimalAPIView.as_view(), name='animal-list'),
    path('Animal/<int:pk>', views.AnimalAPIView.as_view(), name='animal-detail'),
    path('Animal', )
]