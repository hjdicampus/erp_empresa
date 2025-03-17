from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta
from .forms import VentaForm

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/venta_list.html', {'ventas': ventas})

def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'ventas/venta_form.html', {'form': form})

def venta_edit(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/venta_form.html', {'form': form})

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_list')
    return render(request, 'ventas/venta_confirm_delete.html', {'venta': venta})