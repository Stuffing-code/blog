"""Defines URL users registration"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # URL avtorizations default
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]