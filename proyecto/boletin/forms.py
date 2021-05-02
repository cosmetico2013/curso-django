from django import forms

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields =["nombre", "email"]
class RegForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()