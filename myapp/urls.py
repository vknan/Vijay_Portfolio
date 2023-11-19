from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user/register/', views.login_functionality.register, name = 'register'),
    path('accounts/login/', views.login_functionality.login, name = 'login'),
    # path('logout/', views.login_functionality.logout, name = 'logout'),
    path('customlogout/', views.login_functionality.customlogout, name='custom_logout'),

    path('', views.pages.home, name = 'home'),
    path('about/', views.pages.about, name = 'about'),
    path('services/', views.pages.services, name = 'services'),
    path('Templates/', views.pages.Templates, name = 'Templates'),
    path('blog/', views.pages.blog, name = 'blog'),
    path('contact/', views.pages.contact, name = 'contact'),
    path('blog_single/<str:title>/', views.pages.blog_single, name = 'blog_single'),
    path('search/', views.pages.search, name = 'search'),
    path('comment/', views.pages.post_comment, name = 'comment'),
    path('termsandconditions/', views.pages.termsandconditions, name = 'termsandconditions'),
    path('privacypolicy/', views.pages.privacypolicy, name = 'privacypolicy'),
    path('refundpolicy/', views.pages.refundpolicy, name = 'refundpolicy'),


    # path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='templates/login_func/password_reset.html'), name='password_reset'),
    # path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='templates/login_func/password_reset_done.html'), name='password_reset_done'),
    # path('accounts/password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='templates/login_func/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('accounts/password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='templates/login_func/password_reset_complete.html'), name='password_reset_complete'),
    
    
    path('download_file/<int:file_id>/', views.PaymentProcess.download_file, name = 'download_file'),
    path('file_detail/<int:file_id>/', views.PaymentProcess.file_detail, name = 'file_detail'),
    path('checkout/', views.PaymentProcess.checkout, name = 'checkout'),
    path('process_order/', views.PaymentProcess.process_order, name = 'process_order'),
    path('placed_order/<int:file_id>/', views.PaymentProcess.placed_order, name = 'placed_order'),

    # path('dashboard/', views.pages.dashboard, name='dashboard'),
    
]
