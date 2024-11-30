from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articulos.models import Article, Category

@login_required(login_url='inicio')
def list_art(request):
    # sacar artículos de BD
    articulos = Article.objects.all()
    return render(request, 'articulos/listado_articulos.html', {
        'title': 'Artículos',
        'content': 'Lista de Artículos',
        'articulos': articulos
    })

@login_required(login_url='inicio')
def list_cat(request):
    categorias = Category.objects.all()
    return render(request, 'categorias/listado_cat.html', {
        'title': 'Categorías',
        'content': 'Lista de Categorías',
        'categorias': categorias
    })
