from django.shortcuts import render
from .forms import RegForm
from .models import Registrado

# Create your views here.

def inicio(request):
	titulo = "HOLA"
	if  request.user.is_authenticated:
		titulo = "Bienvenido %s" %(request.user)
	f orm = RegForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("email")
		abc2 = form_data.get("nombre")
		obj = Registrado.objects.create(email=abc, nombre=abc2)
	context = {
		"titulo" : titulo,
		"el_form" : form,
	}
	return render (request, "inicio.html", context)