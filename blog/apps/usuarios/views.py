from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm, ContactoForm

# Create your views here.

class Registro(CreateView):
    #Forms Django
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/register.html'

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        ContactoForm(data=request.POST).save()

    return render(request, 'contacto/formulario.html', data)