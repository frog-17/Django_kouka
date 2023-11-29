from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'test'
urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register_cancel/', views.Register_cancelView.as_view(), name='register_cancel'),
    path('login_cancel/', views.Login_cancelView.as_view(), name='login_cancel'),
    path('logout/', views.MylogoutView.as_view(), name='logout'),
    path('password_reset/', views.MyPasswordResetView.as_view(template_name='password.html'), name='password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('reset/done/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path(r'reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
