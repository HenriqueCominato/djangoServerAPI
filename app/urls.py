from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consulta/', views.consulta, name='consulta'),
    path('test_connection/', views.test_connection, name='test_connection'),
]