from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(
    'house', 
    views.HouseModelViewSet, 
    basename='house'
)

urlpatterns = [
    path('', include(router.urls)),
]