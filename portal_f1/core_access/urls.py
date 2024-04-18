# -*- encoding: utf-8 -*-

from django.urls import path
from core_access.views import *
from django.contrib.auth.views import LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', LoginView, name="login"),
    
    path('register/', RegisterView, name="register"),
    path('list/user', UserList.as_view(), name="list_user"),

    path('cadastrar/usuario', AccountCreationView.as_view(), name="cadastrar_usuario"),

    path("logout/", LogoutView.as_view(), name="logout"),
    path("editar/usuario/<int:pk>/", ProfileUpdate.as_view(), name="editar_usuario"),
    path("edit/adm/user/<int:pk>/", ProfileAdmUpdate.as_view(), name="edit_adm_user"),
    path('editar/senha/usuario', AccountPasswordChangeView, name='editar_senha_usuario'),

    path('reset_password/', ResetPasswordView, name="reset_password"),
    path('reset_password/sent/', PasswordResetDoneView.as_view(template_name='users/reset_password_sent.html'), name='reset_password_sent'),
    path('reset_password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="users/reset_password_confirm.html"), name='reset_password_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'), name='password_reset_complete'),      
]

