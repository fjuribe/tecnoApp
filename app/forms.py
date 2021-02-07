from django import forms
from .models import Clientes,Alumno,Contacto_ya,Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ClienteForm(forms.ModelForm):
	class Meta:
		model=Clientes
		#fields=["nombre","correo","tipo_consulta","mensaje","avisos"]
		fields='__all__'


class AlumnoForm(forms.ModelForm):
	class Meta:
		model=Alumno
		fields='__all__'


class Contacto_ya_Form(forms.ModelForm):
	#nombre=forms.CharField(max_length=40,widget=forms.TextInput(attrs={"class": "form-control"})),
	class Meta:
		model=Contacto_ya
		fields='__all__'

class ProductoFormulario(forms.ModelForm):
	nombre=forms.CharField(min_length=3,max_length=50)
	imagen=forms.ImageField(required=False,validators=[MaxSizeFileValidator(max_file_size=2)])
	precio=forms.IntegerField(min_value=1,max_value=1500000)

	def clean_nombre(self):
		nombre=self.cleaned_data["nombre"]
		existe=Producto.objects.filter(nombre__iexact=nombre).exists()

		if existe:
			raise ValidationError("Este nombre existe!!")
		return nombre

	class Meta:
		model=Producto
		fields='__all__'

		widgets={
			"fecha_fabricacion":forms.SelectDateWidget()
		}


class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model=User
		#fields=['username','first_name','email','password1','password2']
		fields='__all__'