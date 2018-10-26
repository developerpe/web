from django.db import models
from ckeditor.fields import RichTextField
import math

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de Categoría', max_length = 255, blank = False, null = False)
    estado = models.BooleanField('Activo o No Activo', default = False)
    fecha_creacion = models.DateField('Fecha de creación',auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    id = models.AutoField(primary_key = True)
    comentario = models.TextField('Comentario', blank = False, null = False)
    estado = models.BooleanField('Activo o No Activo', default = False)
    fecha_creacion = models.DateField('Fecha de creación',auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de Autor', max_length = 255, blank = False, null = False)
    apellidos = models.CharField('Apellidos de Autor', max_length = 255, blank = False, null = False)
    facebook = models.URLField('Facebook', blank = True, null = True)
    twitter = models.URLField('Twitter', blank = True, null = True)
    web = models.URLField('Web', blank = True, null = True)
    correo = models.EmailField('Email', blank = True, null = True)
    estado = models.BooleanField('Activo o No Activo', default = False)
    fecha_creacion = models.DateField('Fecha de creación',auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 40, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 255, blank = False, null = False)
    description = models.CharField('Descripción',max_length = 50, null = False, blank = False)
    imagen_previa = models.URLField(max_length = 255, null=False,blank=False)
    contenido = RichTextField()
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    comentarios = models.ManyToManyField(Comentario, blank = True)
    estado = models.BooleanField('Publicado/No Publicado', default = False)
    fecha_creacion = models.DateField('Fecha de creación', blank = True, null = True)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.slug


class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de Persona', max_length = 255, blank = False, null = False)
    apellidos = models.CharField('Apellidos de Persona', max_length = 255, blank = False, null = False)
    comentarios = models.ForeignKey(Comentario, on_delete = models.CASCADE, blank = True, null = True)
    estado = models.BooleanField('Activo o No Activo', default = False)
    fecha_creacion = models.DateField('Fecha de creación',auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
