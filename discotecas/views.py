from django.shortcuts import render, redirect, get_object_or_404
from .models import Discoteca, Sucursal
from .forms import DiscotecaForm

# Vista para listar discotecas
def listar_discotecas(request):
    discotecas = Discoteca.objects.all()
    return render(request, 'discotecas/listar_discotecas.html', {'discotecas': discotecas})

# Vista para crear una nueva discoteca
def crear_discoteca(request):
    if request.method == 'POST':
        form = DiscotecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_discotecas')
    else:
        form = DiscotecaForm()
    return render(request, 'discotecas/crear_discoteca.html', {'form': form})

# Vista para editar una discoteca
def editar_discoteca(request, id):
    discoteca = get_object_or_404(Discoteca, id=id)
    if request.method == 'POST':
        form = DiscotecaForm(request.POST, instance=discoteca)
        if form.is_valid():
            form.save()
            return redirect('listar_discotecas')
    else:
        form = DiscotecaForm(instance=discoteca)
    return render(request, 'discotecas/editar_discoteca.html', {'form': form})

# Vista para eliminar una discoteca
def eliminar_discoteca(request, id):
    discoteca = get_object_or_404(Discoteca, id=id)
    if request.method == 'POST':
        discoteca.delete()
        return redirect('listar_discotecas')
    return render(request, 'discotecas/eliminar_discoteca.html', {'discoteca': discoteca})
