from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(
    'creature', 
    views.CreatureModelViewSet, 
    basename='creature'
)

urlpatterns = [
    path('', include(router.urls)),
]