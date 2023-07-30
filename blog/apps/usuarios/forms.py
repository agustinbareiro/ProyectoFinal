from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Contacto


class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = Usuario
        fields = "__all__"

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"