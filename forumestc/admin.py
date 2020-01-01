from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Departement, Subject, Reponse, utilisateur, theme)
class ViewAdmin(ImportExportModelAdmin):
    pass

class ProfileInline(admin.StackedInline):
    model = utilisateur
    can_delete = False
    verbose_name_plural = 'utilisateur'
    fk_name = 'User'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)