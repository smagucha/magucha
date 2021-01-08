#from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name=""),
    path('about/', views.about, name ='about'),
    path('resume/', views.resume, name = 'resume'),
    path('services/', views.services, name = 'services'),
    path('contact/', views.contact, name = 'contact')
]