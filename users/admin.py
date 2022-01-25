from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser
from django.forms import Textarea
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    
    list_filter = ('email', 'user_name', 'first_name','last_name', 'is_active', 'is_staff','is_student','department')
    ordering = ('id',)
    list_display = ('user_name', 'email', 'id',
                    'first_name','last_name','department', 'is_active', 'is_staff','is_student','is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','last_name','department')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_student','is_admin')}),
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'row': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'user_name', 'first_name','last_name','department','password1', 'password2', 'is_active', 'is_staff','is_student','is_admin')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
