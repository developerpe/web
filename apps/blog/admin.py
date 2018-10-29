from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','nombre','estado','fecha_creacion')
    search_fields = ['nombre']
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','nombre','apellidos','estado','correo','facebook','twitter','fecha_creacion')
    search_fields = ['nombre']
    resource_class = AutorResource

class PersonaResource(resources.ModelResource):
    class Meta:
        model = Persona

class PersonaAdmin(ImportExportModelAdmin):
    resource_class = PersonaResource

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','titulo','slug','autor','categoria','estado','fecha_creacion')
    search_fields = ['titulo']
    resource_class = PostResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Post,PostAdmin)
