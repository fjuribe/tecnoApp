from django.db import models

# Create your models here.
PAISES = [
    ('FRA', 'Francia'),
    ('CHI', 'Chile'),
    ('BRA', 'Brasil'),
    ('ARG', 'Argentina'),
    ('PER', 'Peru'),
]
CONSULTAS= [
    (0, 'consulta'),
    (1, 'reclamo'),
    (2, 'sugerencia'),
    (3, 'felicitaciones'),
]

GENERO= [
    ('H', 'hombre'),
    ('F', 'mujer'),
]

operaciones_consulta=[
	[0,"consulta"],
	[1,"reclamo"],
	[2,"sugerencia"],
	[3,"fecilitaciones"]
]

class Contacto(models.Model):
	nombre=models.CharField(default=None,null=False,max_length=40)
	edad=models.IntegerField(default=0)
	comentario=models.TextField(default=None, null=True)
	direccion=models.CharField(default=None,null=False,max_length=40)
	pais=models.CharField(max_length=3,choices=PAISES)


class Clientes(models.Model):
	nombre=models.CharField(max_length=50)
	correo=models.EmailField()
	tipo_consulta=models.IntegerField(choices=CONSULTAS)
	mensaje=models.TextField()
	avisos=models.BooleanField()


class Alumno(models.Model):
	nombre=models.CharField(default=None,null=False,max_length=40)
	apodo=models.CharField(default=None,null=False,max_length=40)
	telefono=models.IntegerField()
	genero=models.CharField(max_length=1,choices=GENERO)
	picture = models.ImageField(upload_to='media/',blank=True,null=True)



class Marca(models.Model):
	nombre=models.CharField(max_length=50)

	def __str__(self):
		return self.nombre



class Producto(models.Model):
	nombre=models.CharField(max_length=50)
	precio=models.IntegerField()
	descripcion=models.TextField()
	nuevo=models.BooleanField()
	marca=models.ForeignKey(Marca,on_delete=models.PROTECT)
	fecha_fabricacion=models.DateField()
	imagen=models.ImageField(upload_to="productos",null=True)
	def __str__(self):
		return self.nombre


class Contacto_ya(models.Model):
	nombre=models.CharField(max_length=50)
	correo=models.EmailField()
	tipo_consulta=models.IntegerField(choices=operaciones_consulta)
	mensaje=models.TextField()
	avisos=models.BooleanField()

	def __str__(self):
		return self.nombre