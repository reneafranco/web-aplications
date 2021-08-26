
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null', upload_to="articles")
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Articulo",
        verbose_name_plural  = "Articulos",
        ordering = ['-id']
    
    def __str__(self):

        if self.public:
            public  = "publicado"
        else:
            public = "oculto"
        return f"{self.title}  {public} "



class Category(models.Model):
    name = models.CharField(max_length=110)
    descrption = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = "Categoria",
        verbose_name_plural  = "Categorias"
