from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pelicula (models.Model):
    titulo=models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    director=models.CharField(max_length=200, blank=True)
    fecha = models.DateField(null=True)
    descargada=models.BooleanField(default=False, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    reseña=models.TextField(blank=True)


    def __str__(self):
        return self.titulo

class Serie (models.Model):
    titulo=models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    fecha = models.DateField(null=True)
    temporadas= models.IntegerField(default=1)
    completada=models.BooleanField(default=False)
    descargada=models.BooleanField(default=False)
    reseña=models.TextField(blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=True)

    def __str__(self):
        return self.titulo

class Capitulo (models.Model):
    numero= models.IntegerField(default=0)
    nombre= models.CharField(max_length=200)
    descripcion=models.CharField(max_length=500, default="Nuevo Capítulo")
    temporada= models.IntegerField(default=0)
    serie=models.ForeignKey(Serie, on_delete=models.CASCADE)
    visto=models.BooleanField(default=False)
    fecha_emision=models.DateField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    reseña=models.TextField(blank=True)

    def __str__(self):
        return self.serie.titulo +" - by " + self.user.username # + "x" + self.numero

class Documentales (models.Model):
    titulo=models.CharField(max_length=200)
    maker=models.CharField(max_length=200, blank=True)
    fecha = models.DateField
    descargada=models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.serie.titulo
  
""""
    pelicula=Pelicula(titulo='Rocky', director= 'Sylvester Stallone')
    pelicula.save()
    lista_peliculas = Pelicula.objects.aall()
    print(lista_pelicula)

    pelicula= Pelicula.objects.get(titulo='Rocky')
    print(pelicula.titulo)

    pelicula= Pelicula.objects.get(titulo='Rocky')
    pelicula.delete

    pelicula= Pelicula.objects.get(titulo='Rocky')
    pelicula.director='otro'
    pelicula.save()
"""