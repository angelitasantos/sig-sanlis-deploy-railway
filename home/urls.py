from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
]
