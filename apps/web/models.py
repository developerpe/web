from django.db import models

class Aprender(models.Model):
	id = models.AutoField(primary_key = True)
	titulo = models.CharField('Título',max_length = 255, null = False,blank = False)
	descripcion = models.TextField('Descripción')

	class Meta:
		verbose_name = 'Aprender'
		verbose_name_plural = 'Aprendes'

	def __str__(self):
		return self.titulo

class Web(models.Model):
	id = models.AutoField(primary_key = True)
	slogan = models.CharField('Slogan',max_length = 255, null = False,blank = False)
	nosotros = models.TextField('Nosotros')
	aprenderas_slogan = models.CharField('Aprenderás Slogan',max_length = 255, null = False,blank = False)
	aprender_id = models.ManyToManyField(Aprender)

	class Meta:
		verbose_name = 'Web'
		verbose_name_plural = 'Webs'

	def __str__(self):
		return self.slogan

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Cliente(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField('Nombre de Cliente', max_length = 255, blank = False, null = False)
	cargo = models.CharField('Cargo', max_length = 255, blank = False, null = False)
	mensaje = models.TextField('Mensaje')
	url_image = models.ImageField('Imagen', upload_to=upload_location,
		null=True,blank=True,
		height_field = "height_field",
		width_field = "width_field"
	)
	height_field = models.IntegerField(default = 400)
	width_field = models.IntegerField(default = 400)
	estado = models.BooleanField('Estado', default = False)

	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'

	def __str__(self):
		return self.nombre

class Suscripcion(models.Model):
	id = models.AutoField(primary_key = True)
	correo = models.EmailField('Correo electrónico')
	estado = models.BooleanField('Estado', default = False)

	def __str__(self):
		return self.correo

class Contacto(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField('Nombre de Cliente', max_length = 255, blank = False, null = False)
	correo = models.EmailField('Correo electrónico')
	asunto = models.CharField('Asunto', max_length = 255, blank = False, null = False)
	mensaje = models.TextField('Mensaje', max_length = 255, blank = False, null = False)

	class Meta:
		verbose_name = 'Contacto'
		verbose_name_plural = 'Contactos'

	def __str__(self):
		return self.asunto
