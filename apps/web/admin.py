from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AprenderResource(resources.ModelResource):
    class Meta:
        model = Aprender

class AprenderAdmin(ImportExportModelAdmin):
    resource_class = AprenderResource

class WebResource(resources.ModelResource):
    class Meta:
        model = Web

class WebAdmin(ImportExportModelAdmin):
    resource_class = WebResource

class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente

class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','nombre','cargo','estado','fecha_creacion')
    search_fields = ['nombre']
    resource_class = ClienteResource

class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto

class ContactoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','nombre','correo','asunto','fecha_creacion')
    search_fields = ['nombre']
    resource_class = ContactoResource

class SuscripcionResource(resources.ModelResource):
    class Meta:
        model = Suscripcion

class SuscripcionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','correo','estado','fecha_creacion')
    search_fields = ['correo']
    resource_class = SuscripcionResource

admin.site.register(Aprender,AprenderAdmin)
admin.site.register(Web,WebAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Suscripcion,SuscripcionAdmin)
