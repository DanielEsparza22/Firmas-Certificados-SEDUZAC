from django.urls import path
from . import views

urlpatterns = [
    path('',views.logear,name="Login"),
    path('cerrar_sesion',views.cerrar_sesion,name="cerrar_sesion"),
]