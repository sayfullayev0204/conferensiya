from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'address', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        # (None, {'fields': ('birthday',)}),
        (None, {'fields': ('address',)}),

    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        # (None, {'fields':('birthday',)}),
        (None, {'fields': ('address',)}),

    )

admin.site.register(CustomUser, CustomUserAdmin)