from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('produtos/', views.produtos_view, name='produtos'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('status/', views.status_view, name='status'),
]