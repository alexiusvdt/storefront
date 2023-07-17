from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User

# jank
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin


class UserAdmin(BaseUserAdmin):
    #    fieldsets = (
    #        (None, {'fields': ('email', 'password', )}),
    #        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    #        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                       'groups', 'user_permissions')}),
    #        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    #          (_('user_info'), {'fields': ('first_name', 'last_name', 'phone_no')}),
    #    )
    #    add_fieldsets = (
    #        (None, {
    #            'classes': ('wide', ),
    #            'fields': ('email', 'password1', 'password2'),
    #        }),
    #    )
    ordering = ("email",)


admin.site.register(User, UserAdmin)
