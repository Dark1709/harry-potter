from django.urls import path
from . import views

urlpatterns = [
    path('Users', views.UserList.as_view(), name='user-list'),
]