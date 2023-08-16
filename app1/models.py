from django.db import models

class Cliente(models.Model):
    nombre_cli = models.CharField( max_length=40) 
    apellido_cli = models.CharField(max_length=40)    
    telefono_cli= models.IntegerField()
    mail= models.EmailField(max_length=50)

class Animal(models.Model):
    nombre_mas = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad=models.IntegerField()
    dueño=models.CharField(max_length=40)

class Veterinario (models.Model):
    nombre_vet = models.CharField(max_length=40) 
    apellido_vet = models.CharField(max_length=40)    
    telefono_vet=models.IntegerField()
    legajo=models.IntegerField()