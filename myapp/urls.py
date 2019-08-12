from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_list, name='base_list'),
]