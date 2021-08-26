from django.contrib import admin
from .models import Article, Category 

#Para mostrar campos de solo lectura haces esto 
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)


#Configurar el titulo del panel de administracion
admin.site.site_header = "Máster en Python"
admin.site.site_title = "Master-admin"
admin.site.index_title = "Python-Master"