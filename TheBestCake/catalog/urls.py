from django.urls import path
from . import views
from .views import ListaProductos,DetalleProducto,ComentarioProducto,AniadirCarrito,ListarCarrito,ListarCarritoPendientes,ListarCarritoFinalizadas,EliminarCarrito,DetallePago

urlpatterns = [
    path('', views.product, name="catalog"),
    path('listaProductos/', ListaProductos.as_view(), name="listaProductos"),
    path('detalleProductos/<int:pk>/', DetalleProducto.as_view(), name="detalleProductos"),
    path('crearComentario/', ComentarioProducto.as_view(), name="crearComentario"),
    path('aniadirCarrito/', AniadirCarrito.as_view(), name="aniadirCarrito"),
    path('listarCarrito/',ListarCarrito.as_view(),name='listarCarrito'),
    path('listarPendientes/',ListarCarritoPendientes.as_view(),name='listarPendientes'),
    path('listarFinalizados/',ListarCarritoFinalizadas.as_view(),name='listarFinalizados'),
    path('eliminarCarrito/<int:pk>/',EliminarCarrito.as_view(),name='eliminarCarrito'),
    path('detallePago/',DetallePago.as_view(),name='detallePago'),
]
