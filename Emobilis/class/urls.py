from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home page'),
    path('about/', views.about, name='about page'),
    path('contacts/', views.contacts, name='contacts page'),
    path('shops/', views.shops, name='shops page')

]