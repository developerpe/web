from django.shortcuts import render,redirect
from .models import *
from .forms import SuscripcionForm,ContactoForm
from django.http import HttpResponse

def home(request):
	queryset = Web.objects.all()
	clientes = Cliente.objects.filter(estado = True)
	if request.method == 'POST':
		if request.is_ajax():
			form = SuscripcionForm(request.POST)
			if form.is_valid():
				form.save()
				message = "Done"
			else:
				form = SuscripcionForm()
				message = "Error"
			return HttpResponse(message)
	return render(request,'web/index.html',{'queryset':queryset,'clientes':clientes})

def Contact(request):
	if request.method == 'POST':
		if request.is_ajax():
			form = ContactoForm(request.POST)
			if form.is_valid():
				form.save()
				message = "Formulario enviado."
			else:
				form = ContactoForm()
				message = "Error"
			return HttpResponse(message)
