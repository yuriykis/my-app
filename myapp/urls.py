from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base_list'),
    path('osoba/<int:pk>/', views.entity_detail, name='entity_detail'),
    path('osoba/new', views.osoba_new, name='osoba_new'),
    path('osoba/<int:pk>/telefon', views.add_os_tel, name='add_os_tel'),
    path('osoba/<int:pk>/mail', views.add_os_mail, name='add_os_mail'),
    path('osoba/<int:pk>/edit', views.osoba_edit, name='osoba_edit'),
    path('osoba/<int:pk>/detele>', views.osoba_delete, name='osoba_delete'),
    path('osoba/szukaj', views.osoba_szukaj, name = 'osoba_szukaj'),
]