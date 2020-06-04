from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_user_form = UserAdminCreationForm
    change_form = UserAdminChangeForm


    list_display = ('email', 'full_name', 'is_active', 'is_admin')
    list_filter = ('is_admin','is_staff', 'is_active')


    fieldsets = (
        (None, {'fields': ('email', 'password')}), # These fields appear at the top
        ('Personal info', {'fields': ('full_name',)}),   # these fields appear under personal info
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'full_name')


    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(User,UserAdmin)