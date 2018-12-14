from django.shortcuts import render, redirect
from .forms import RegistrarTec
from .models import Asignar
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def tec_list(request):
    return render(request, 'base/base.html', {})

def registro_tec(request):
    if request.method == 'POST':
        form = RegistrarTec(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ah reggistrado Usuario correctamente')
            return redirect('tecnico:index')
    else:
        form = RegistrarTec()
    return render(request, 'tecnico/registrar.html', {'form':form})

