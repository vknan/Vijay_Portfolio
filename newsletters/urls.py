from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('subscribe/', views.newsletters.subscribe, name='subscribe'),
    path('success/', views.newsletters.success_page, name='success_page'),
]
