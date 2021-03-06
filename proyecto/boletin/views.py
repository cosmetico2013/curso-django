from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.

def inicio(request):
	titulo = "Bienvenido"
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
	
	if request.user.is_authenticated and request.user.is_staff:
		queryset = Registrado.objects.all().order_by("-timestamp")
		context = {
			"queryset": queryset,
		}
	return render (request, "inicio.html", context)

def contact(request):
	titulo = "Contacto"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key, value in form.cleaned_data.iteritems():
		#	print (key, value)
		#for key in form.cleaned_data:
		#	print key
		#	print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = "Form de contacto"
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otroemail@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)

		#print email, mensaje nombre
	context = {
		"form": form,
		"titulo": titulo,
	}
	return render(request, "forms.html", context)