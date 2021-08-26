import re
from django.http.response import HttpResponseServerError
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q 
from miapp.forms import FormArticle
from django.contrib import  messages

# Create your views here.
#MVC = MOdelo Vista Controlador -> Acciones(Metodos)
#MVT = Modelo Template Vista -> Acciones(Metodos)

#Puedes hacerte una pequeña plantilla para navegar entre las vistas
layout = """


"""

#Crear tu primera vista q son funciones

def index(request):

    nombre = 'Rene Adonay'
    lenguajes = ['Python', 'Js', 'PHP', "C++", "C"]
    years = 2021
    rango = range(years, 2051)

    return render(request, 'index.html', {
        'title': 'Home Page',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': years,
        'rango': rango
    })

def hola_mundo(request): #el request es un parametro q me permite recibir datos de peticiones a esta url
    #tienes q pasarle el parametro request a cada una de las funciones q hagas en views
    #Aqui puedo usar 3comillas y hacer un html dentro de la funcion
    return render(request,'hola_mundo.html')
   

def test(request, redirigir=0):

    years = 2021

    rango = range(years, 2051)
    return render(request,'test.html',{
        'years': years,
        'rango': rango
    })

     
def contacto(request, nombre="", apellidos=""):
    return render(request,'contacto.html')

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content, 
        public =public
    )

    articulo.save()

    return  HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} ")


def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content, 
            public =public
        )   

        articulo.save() 
        
        return  HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} ")
 
    else:
        return  HttpResponse("<h2>No se ha podido Guardar nada</h2>")


    return  HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} ")

def create_article(request):

    return render(request, 'create_article.html')



def create_full_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title   = data_form.get('title'),
            content = data_form['content'],
            public  = data_form['public']
            
            articulo = Article(
                title = title ,
                content = content , 
                public =public
        )   

            articulo.save() 

            #crear mensaje flash(secion q solo se muestra una vez)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id} ')

            return redirect('Articulos')
            #return HttpResponse(str(articulo.title) + str(articulo.content) + str(articulo.public))

    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })


def articulo(request):
    
    articulo = Article.objects.get(title="Tercer_contenido")
    
    return HttpResponse(f"Articulo: {articulo.id} - {articulo.title}")

def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula de DC el caballero de la noche"
    articulo.public = True 

    articulo.save()

    return HttpResponse(f"Articulo editado: {articulo.title} ")

def articulos(request):

    articulos = Article.objects.all()

    articulos = Article.objects.filter(public=True).order_by('-id')

    """articulos = Article.objects.filter()

    articulos = Article.objects.filter(id__gte=10, title__contains="articulo")

    articulos = Article.objects.filter(
                    title="articulo").exclude(public=True)

    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='articulo2' AND public=1 ")
    articulos = Article.objects.filter(
        Q(title__contains="") | Q(title__contains="")
    )
    
    )"""

    return render(request, 'articulos.html', {
        'articulos': articulos
    } )

def borrar_articulo(request, id):

    articulo = Article.objects.get(pk=id)    
    articulo.delete()

    return redirect('Articulos')