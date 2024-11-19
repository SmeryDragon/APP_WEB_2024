from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    
    return render(request, "mainapp/index.html", {
        'title':'Inicio ',
        'content':'Bienvenido al inicio'} )
    
def about(request):
    return render(request, "mainapp/about.html", {
        'title':'Acerca de ',
        'content':'Soy Acerca de '} )
    
def mision(request):
    return render(request, "mainapp/mision.html", {
        'title':'Mision ',
        'content':'Soy Misión '} )

def vision(request):
    return render(request, "mainapp/vision.html", {
        'title':'Visión',
        'content':'Soy Misión '} )

def redirigir_inicio (request, exeption=None):
    return redirect('inicio')

def redirigir_inicio(requets,exeption):
    return render(request,'mainapp/404.html')