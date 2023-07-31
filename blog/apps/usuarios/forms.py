from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Contacto


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = Usuario
        fields = {
            'email',
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            # 'avatar'
        }

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"