from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This is the home page URL pattern
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
