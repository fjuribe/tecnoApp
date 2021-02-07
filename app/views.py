from django.shortcuts import render,redirect,get_object_or_404
from app.models import Contacto,Producto
from .forms import ClienteForm,AlumnoForm,Contacto_ya_Form,ProductoFormulario,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import login,authenticate
# Create your views here.


def home(request):
	productos=Producto.objects.all()
	data={
		'productos':productos
	}
	return render(request,'app/sitio/home.html',data)


def contacto2(request):
	data={
		'form':Contacto_ya_Form()
	}
	if request.method=='POST':
		formulario=Contacto_ya_Form(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"]="se guardo correctamente"
		else:
			data["form"]=formulario

	return render(request,'app/sitio/contacto.html',data)

def galeria2(request):
	return render(request,'app/sitio/galeria.html')



def agregar_producto(request):
	data={
		'form':ProductoFormulario()
	}
	if request.method=='POST':
		formulario=ProductoFormulario(data=request.POST,files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"]="se guardo correctamente"
		else:
			data["form"]=ProductoFormulario
		
	return render(request,'app/sitio/producto/agregar.html',data)


def listar_productos(request):
	producto=Producto.objects.all()
	page=request.GET.get('page',1)

	try:
		paginator=Paginator(producto,2)
		producto=paginator.page(page)
	except:
		raise Http404

	data={
		'entity':producto,
		'paginator':paginator
	}
	return render(request,'app/sitio/producto/listar.html',data)	

def modificar_producto(request,id):
	producto=get_object_or_404(Producto,id=id)
	#Producto.objects.get(id=id)

	data={
		'form':ProductoFormulario(instance=producto)
	}

	if request.method=='POST':
		formulario=ProductoFormulario(data=request.POST,instance=producto,files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			messages.success(request,"modificado correctamente")
			return redirect(to='listar-producto')
		data["form"]=formulario
	return render(request,'app/sitio/producto/modificar.html',data)



def eliminar(request,id):
	producto=get_object_or_404(Producto,id=id)
	producto.delete()
	messages.success(request,"elimindo correctamente")
	return redirect(to='listar-producto')

def registro(request):
	data={
		'form':CustomUserCreationForm()
	}
	if request.method=='POST':
		formulario=CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
			login(request,user)
			messages.success(request,"Te has registrado correctamente!!")
			return redirect(to="home")
		data['form']=formulario
	return render(request,'registration/registro.html',data)







##################################################3
def formulario(request):
	return render(request,'app/contacto.html')


def contacto(request):
	if request.method=="POST":
		nombre=request.POST['nombre']
		edad=request.POST['edad']
		comentario=request.POST['comentario']
		direccion=request.POST['direccion']
		pais=request.POST['pais']

		Contacto.objects.create(nombre=nombre,edad=edad,comentario=comentario,direccion=direccion,pais=pais)
		print(f"aqui ----->{request.method}")
		# obj={
		# 	'nombre':nombre,
		# 	'edad':edad,
		# 	'comentario':comentario,
		# 	'direccion':direccion,
		#     'pais':pais,
		# }
		
	return render(request,'app/galeria.html',{'mensaje':'AGREGADO'})

def galeria(request):
	return render(request,'app/galeria.html')


def clientes(request):
	data={
		'form':ClienteForm()
	}
	if request.method=='POST':
		cliente=ClienteForm(data=request.POST)
		if cliente.is_valid():
			print("hola")
			cliente.save()
			data['success']="datos guardados!!"
		else:
			data['form']=cliente

	return render(request,'app/cliente.html',data)



def alumno(request):

	if request.method=='POST':
		form=AlumnoForm(request.POST,request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			form.nombre=data['nombre']
			form.apodo=data['apodo']
			form.telefono=data['telefono']
			form.genero=data['genero']
			form.save()

			return redirect('home')
	else:
		form=AlumnoForm()

	return render(request,'app/alumno.html',context={'form':form})