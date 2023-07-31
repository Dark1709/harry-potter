from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(
    'character', 
    views.CharacterModelViewSet, 
    basename='character'
)

urlpatterns = [
    path('', include(router.urls)),
    # path('characters', views.CharacterAPIView.as_view(), name='character-list'),
    # path('characters/<int:pk>', views.CharacterAPIView.as_view(), name='character-detail'),
]