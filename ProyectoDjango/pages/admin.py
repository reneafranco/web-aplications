
from django.contrib import admin
from .models import Page
from django.conf import settings

#configuracion para el panel de administracion 
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    #crear un buscador
    search_fields = ('title', 'content')
    list_filter = ('visible', )
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)


#Mostrar articulos de solo lectuta como created_at
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


# Register your models here.
admin.site.register(Page, PageAdmin)


#Cambiar titulo y subtitulos a el panel de administracion

admin.site.site_header = "Panel de Gestion"
admin.site.site_title = "Pages"
admin.site.index_title = "Gestor"

