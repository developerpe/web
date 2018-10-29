from django.shortcuts import render,HttpResponse
from .models import *
from django.views.generic import TemplateView
import re,random
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

DATE_REGEX=re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$')


class Home_blog(TemplateView):
	def get(self,request,*args,**kwargs):
		posts = Post.objects.filter(
			estado = True
		)
		paginator = Paginator(posts, 6)
		page = request.GET.get('page')
		post = paginator.get_page(page)

		content = {
			'post':post
		}
		return render(request,'blog/index.html',content)
	"""
	num_pages = int(len(post)/6)
	if (len(post)%6!=0):
		num_pages += 1
	pages = []
	for i in range(1, num_pages+1):
		pages.append(i)
	content = {
		'post':post,
		'pages':pages
	}
	content['post'] = content['post'][0:6]
	"""
def Prueba(request):
	if(request.method!='POST'):
		return HttpResponse('404 NON FOUND')
	context={}
	search_words = request.POST['search_name'].split()
	if(len(search_words)==1):
		search_words.append('')
	if(len(request.POST['search_name'])==0):
		context['post'] = Post.objects.filter(
			estado = True
		)
	else:
		context['post'] = Post.objects.filter(
			estado = True,titulo__startswith = search_words[0]
		)
	page_num = int(request.POST['page_num'])
	context['post'] = context['post'][(page_num-1)*6:page_num*6]
	return render(request,'blog/post.html',context)

class Detail_Post(TemplateView):
	def get(self,request,slug,*args,**kwargs):
		post_detail = Post.objects.get(slug=slug)
		number_post = len(Post.objects.filter(estado = True))
		number = random.randint(1, (number_post-1))
		if number == post_detail.id:
			number = random.randint(1, (number_post-1))
		print(number)
		post_detail2 = Post.objects.get(
			id = number
		)
		post_detail3 = Post.objects.get(
			id = (number+1)
		)
		print(post_detail2)
		print(post_detail3)
		content = {
			'post_detail': post_detail,
			'post_detail2': post_detail2,
			'post_detail3': post_detail3
		}
		return render(request,'blog/detail_post.html',content)


def Prueba_movil(request):
	if(request.method!='POST'):
		return HttpResponse('404 NON FOUND')
	context={}
	search_words = request.POST['search_name'].split()
	categoria = Categoria.objects.get(nombre = 'Movil')
	if(len(search_words)==1):
		search_words.append('')
	if(len(request.POST['search_name'])==0):
		context['post'] = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
	else:
		context['post'] = Post.objects.filter(
			estado = True,titulo__startswith = search_words[0],categoria = categoria
		)
	page_num = int(request.POST['page_num'])
	context['post'] = context['post'][(page_num-1)*6:page_num*6]
	return render(request,'blog/post.html',context)

class Blog_movil(TemplateView):
	def get(self,request,*args,**kwargs):
		categoria = Categoria.objects.get(nombre = 'Movil')
		posts = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
		paginator = Paginator(posts, 6)
		page = request.GET.get('page')
		post = paginator.get_page(page)

		content = {
			'post':post
		}
		return render(request,'blog/movil.html',content)

def Prueba_general(request):
	if(request.method!='POST'):
		return HttpResponse('404 NON FOUND')
	context={}
	search_words = request.POST['search_name'].split()
	categoria = Categoria.objects.get(nombre = 'General')
	if(len(search_words)==1):
		search_words.append('')
	if(len(request.POST['search_name'])==0):
		context['post'] = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
	else:
		context['post'] = Post.objects.filter(
			estado = True,titulo__startswith = search_words[0],categoria = categoria
		)
	page_num = int(request.POST['page_num'])
	context['post'] = context['post'][(page_num-1)*6:page_num*6]
	return render(request,'blog/post.html',context)


class Blog_general(TemplateView):
	def get(self,request,*args,**kwargs):
		categoria = Categoria.objects.get(nombre = 'General')
		posts = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
		paginator = Paginator(posts, 6)
		page = request.GET.get('page')
		post = paginator.get_page(page)

		content = {
			'post':post
		}
		return render(request,'blog/generales.html',content)

def Prueba_tecnologia(request):
	if(request.method!='POST'):
		return HttpResponse('404 NON FOUND')
	context={}
	search_words = request.POST['search_name'].split()
	categoria = Categoria.objects.get(nombre = 'Tecnologia')
	if(len(search_words)==1):
		search_words.append('')
	if(len(request.POST['search_name'])==0):
		context['post'] = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
	else:
		context['post'] = Post.objects.filter(
			estado = True,titulo__startswith = search_words[0],categoria = categoria
		)
	page_num = int(request.POST['page_num'])
	context['post'] = context['post'][(page_num-1)*6:page_num*6]
	return render(request,'blog/post.html',context)

class Blog_tecnologia(TemplateView):
	def get(self,request,*args,**kwargs):
		categoria = Categoria.objects.get(nombre = 'Tecnologia')
		posts = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
		paginator = Paginator(posts, 6)
		page = request.GET.get('page')
		post = paginator.get_page(page)

		content = {
			'post':post
		}
		return render(request,'blog/tecnologia.html',content)

def Prueba_programacion(request):
	if(request.method!='POST'):
		return HttpResponse('404 NON FOUND')
	context={}
	search_words = request.POST['search_name'].split()
	categoria = Categoria.objects.get(nombre = 'Programacion')
	if(len(search_words)==1):
		search_words.append('')
	if(len(request.POST['search_name'])==0):
		context['post'] = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
	else:
		context['post'] = Post.objects.filter(
			estado = True,titulo__startswith = search_words[0],categoria = categoria
		)
	page_num = int(request.POST['page_num'])
	context['post'] = context['post'][(page_num-1)*6:page_num*6]
	return render(request,'blog/post.html',context)

class Blog_programacion(TemplateView):
	def get(self,request,*args,**kwargs):
		categoria = Categoria.objects.get(nombre = 'Programacion')
		posts = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
		paginator = Paginator(posts, 6)
		page = request.GET.get('page')
		post = paginator.get_page(page)

		content = {
			'post':post
		}
		return render(request,'blog/programacion.html',content)

def Prueba_videojuegos(request):
	if(request.method!='POST'):
		return HttpResponse('404 NON FOUND')
	context={}
	search_words = request.POST['search_name'].split()
	categoria = Categoria.objects.get(nombre = 'Videojuegos')
	if(len(search_words)==1):
		search_words.append('')
	if(len(request.POST['search_name'])==0):
		context['post'] = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
	else:
		context['post'] = Post.objects.filter(
			estado = True,titulo__startswith = search_words[0],categoria = categoria
		)
	page_num = int(request.POST['page_num'])
	context['post'] = context['post'][(page_num-1)*6:page_num*6]
	return render(request,'blog/post.html',context)


class Blog_videojuegos(TemplateView):
	def get(self,request,*args,**kwargs):
		categoria = Categoria.objects.get(nombre = 'Videojuegos')
		posts = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
		paginator = Paginator(posts, 6)
		page = request.GET.get('page')
		post = paginator.get_page(page)

		content = {
			'post':post
		}
		return render(request,'blog/videojuegos.html',content)

def Prueba_tutoriales(request):
	if(request.method!='POST'):
		return HttpResponse('404 NON FOUND')
	context={}
	search_words = request.POST['search_name'].split()
	categoria = Categoria.objects.get(nombre = 'Tutoriales')
	if(len(search_words)==1):
		search_words.append('')
	if(len(request.POST['search_name'])==0):
		context['post'] = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
	else:
		context['post'] = Post.objects.filter(
			estado = True,titulo__startswith = search_words[0],categoria = categoria
		)
	page_num = int(request.POST['page_num'])
	context['post'] = context['post'][(page_num-1)*6:page_num*6]
	return render(request,'blog/post.html',context)

class Blog_tutoriales(TemplateView):
	def get(self,request,*args,**kwargs):
		categoria = Categoria.objects.get(nombre = 'Tutoriales')
		posts = Post.objects.filter(
			estado = True,
			categoria = categoria
		)
		paginator = Paginator(posts, 6)
		page = request.GET.get('page')
		post = paginator.get_page(page)

		content = {
			'post':post
		}
		return render(request,'blog/tutoriales.html',content)
