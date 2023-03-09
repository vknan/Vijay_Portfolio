from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
    path('user/register/', views.register, name = 'register'),
    path('user/login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('blog_single/<str:title>/', views.blog_single, name = 'blog_single'),
    path('search/', views.search, name = 'search'),
    path('comment/', views.post_comment, name = 'comment'),
]