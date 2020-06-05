from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('',views.home, name = 'home' ),
    path('register/',views.Register, name = 'Register' ),
    path('login/', views.loginPage, name = 'loginPage'),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'UserModule/password_reset.html'), name = 'reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name = 'UserModule/password_reset_sent.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'UserModule/password_new.html'), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'UserModule/password_reset_complete.html'), name = 'password_reset_complete'),

    path('logout/', views.logoutUser, name = "logoutUser"),
    path('user/', views.User_Profile, name = "User_Profile"),

]
