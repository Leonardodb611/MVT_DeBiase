from django.urls import path
from App import views

urlpatterns = [
    path("", views.familia, name="inicio"),
    path("inicio", views.familia, name="Inicio"),
    
   
]