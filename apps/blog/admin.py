from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin):
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin):
    resource_class = AutorResource

class PersonaResource(resources.ModelResource):
    class Meta:
        model = Persona

class PersonaAdmin(ImportExportModelAdmin):
    resource_class = PersonaResource

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Post,PostAdmin)
