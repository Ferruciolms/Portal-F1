from django.contrib import admin
from core_access.models import User
from django.contrib.auth import admin as auth_admin

# Register your models here.
@admin.register(User)
class AccountAdmin(auth_admin.UserAdmin):
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("cpf", "telephone", "login_disabled")}),
    )