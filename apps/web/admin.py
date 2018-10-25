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

class ClienteAdmin(ImportExportModelAdmin):
    resource_class = ClienteResource

class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto

class ContactoAdmin(ImportExportModelAdmin):
    resource_class = ContactoResource

class SuscripcionResource(resources.ModelResource):
    class Meta:
        model = Suscripcion

class SuscripcionAdmin(ImportExportModelAdmin):
    resource_class = SuscripcionResource

admin.site.register(Aprender,AprenderAdmin)
admin.site.register(Web,WebAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Suscripcion,SuscripcionAdmin)
