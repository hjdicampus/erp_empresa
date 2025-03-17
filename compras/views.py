from django.shortcuts import render, redirect, get_object_or_404
from .models import Compra, Producto
from .forms import CompraForm

def compra_list(request):
    compras = Compra.objects.all()
    return render(request, 'compras/compra_list.html', {'compras': compras})

def compra_create(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra_list')
    else:
        form = CompraForm()
    return render(request, 'compras/compra_form.html', {'form': form})

def compra_edit(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('compra_list')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'compras/compra_form.html', {'form': form})

def compra_delete(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        compra.delete()
        return redirect('compra_list')
    return render(request, 'compras/compra_confirm_delete.html', {'compra': compra})