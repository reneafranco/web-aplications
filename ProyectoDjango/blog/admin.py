from django.contrib import admin
from .models import Article, Category

#Crea Clase con campos solo lectura
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


#configuracion para el panel de administracion 
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    #crear un buscador
    search_fields = ('title', 'content')
    list_filter = ('visible', )
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user' ,'public', 'created_at')
    list_filter = ('public','user__username', 'categories__name' )
    
    #crear funcion para guardar articulo con usuario autodectatble
    def save_model(self, request, obj, form , chage):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()



# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
