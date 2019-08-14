from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_list, name='base_list'),
    path('osoba/<int:pk>/', views.entity_detail, name='entity_detail'),
    path('osoba/new', views.osoba_new, name='osoba_new'),
    path('osoba/<int:pk>/edit', views.osoba_edit, name='osoba_edit'),
    path('osoba/<int:pk>/detele>', views.osoba_delete, name='osoba_delete'),
]