from django.shortcuts import render, redirect
from app.orden.forms import OrdenForm
from app.orden.models import Orden
# Create your views here.
def order_list(request):
    return render(request, 'base/base.html', {})

def order_li(request):
    orden = Orden.objects.all()
    contexto = {'ordens':orden}
    return render(request, 'orden/orden_list.html', contexto)

def orden_crear(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tecnico:index')
    else:
        form = OrdenForm()
    
    return render(request, 'orden/orden_form.html', {'form':form})