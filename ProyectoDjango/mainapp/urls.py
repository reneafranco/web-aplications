from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('index/', views.index, name="Inicio"),
    path('registro/',views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
    
]
