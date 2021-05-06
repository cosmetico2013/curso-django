from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.

def inicio(request):
	titulo = "HOLA"
	if  request.user.is_authenticated:
		titulo = "Bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)
	
	context = {
				"titulo" : titulo,
				"el_form" : form,
			}

	if form.is_valid():
		instance = form.save(commic=False)
		if not instance.nombre:
			instance.nombre = "Persona" 
		instance.save()

		context = {
			"titulo" : "Gracias %s" %(instance.nombre)
		}

		if not nombre:
			context = {
				"titulo": "gracias %s" %(instance.email)
			}
#		form_data = form.cleaned_data
#		abc = form_data.get("email")
#		abc2 = form_data.get("nombre")
#		obj = Registrado.objects.create(email=abc, nombre=abc2)
	
	return render (request, "inicio.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key, value in form.cleaned_data.iteritems():
		#	print key, value
		#for key in form.cleaned_data:
		#	print key
		#	print form.cleaned_data.get(key)
		#email = form.cleaned_data.get("email")
		#mensaje = form.cleaned_data.get("mensaje")
		#nombre = form.cleaned_data.get("nombre")
		#print email, mensaje nombre
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)