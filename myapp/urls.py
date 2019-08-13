from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_list, name='base_list'),
    path('osoba/<int:pk>/', views.entity_detail, name='entity_detail'),
]