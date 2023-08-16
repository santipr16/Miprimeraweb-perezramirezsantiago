from django import forms

class FormularioCliente(forms.Form):
    nombre_cli = forms.CharField( max_length=100) 
    apellido_cli = forms.CharField(max_length=100)    
    telefono_cli= forms.IntegerField()
    mail= forms.EmailField(max_length=100)

class FormularioVeterinario (forms.Form):
    nombre_vet = forms.CharField(max_length=40) 
    apellido_vet = forms.CharField(max_length=40)    
    telefono_vet=forms.IntegerField()
    legajo=forms.IntegerField()

class FormularioMascota(forms.Form):
    nombre_mas = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=40)
    raza = forms.CharField(max_length=40)
    edad=forms.IntegerField()
    dueño=forms.CharField(max_length=40)

class MascotaSearchForm(forms.Form):
    nombre = forms.CharField(required=False)