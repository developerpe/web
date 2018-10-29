from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','username','email','first_name','last_name','editor','is_active')
    resource_class = UserResource

admin.site.register(User,UserAdmin)
