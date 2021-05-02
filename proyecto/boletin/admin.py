from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado
class AdminRegistrado(admin.ModelAdmin):
	list_display = ["email", "nombre", "timestamp"]
	form = RegModelForm #modelo del formulario
	#list_display_links = ["nombre"] #campo que tienen el link hacia la cuenta del usuario
	list_filter = ["timestamp"]
	list_editable = ["nombre"] #campo que se permite modificar
	search_fiels = ["email", "nombre"] #campos que se pueden buscar
#	class Meta:
#		model = Registrado

admin.site.register(Registrado, AdminRegistrado)