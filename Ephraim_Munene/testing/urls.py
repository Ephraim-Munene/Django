from django.urls import path
from testing import views

URLPATTERNS = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert')
]