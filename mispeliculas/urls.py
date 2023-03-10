from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),#si dejo el patho en blanco, le estoy diciendo que va a ser en la pàgina de inicio (cuando se visite el local host)
    path('signup/', views.signup, name="signup"),
    path('logout/', views.signout, name="logout"),
    path('signin/', views.signin, name="signin"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('serie/', views.series, name="series"),
    path('capitulo/', views.capitulos, name="capitulos"),
    path('pelicula/', views.peliculas, name="peliculas"),
    path('crearCapitulo/', views.crear_capitulo, name="crearCapitulo"),
    path('detalleCapitulo/<int:capitulo_id>/', views.detalle_capitulo, name="detalleCapitulo"),
    path('detalleCapitulo/<int:capitulo_id>/delete', views.delete_capitulo, name="deleteCapitulo"),
    path('crearSerie/', views.crear_serie, name="crearSerie"),
    path('crearPelicula/', views.crear_pelicula, name="crearPelicula"),
    ]