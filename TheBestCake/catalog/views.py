from django.shortcuts import render
from .models import Design,Comentario,CarritoCompras
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from django.db.models import Q, Max, Min #para hacer consultas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

# Creando vistas
def product(request):
    designs = Design.objects.all()
    return render(request, 'catalog/catalog.html', {'designs':designs})

class ListaProductos(ListView):
    template_name = 'catalog/catalogo_lista.html'
    model = Design
    paginate_by = 4

    def get_queryset(self):
        query = None

        if ('name' in self.request.GET) and self.request.GET['name'] != "":
            query = Q(name=self.request.GET["name"])

        if ('maximo' in self.request.GET) and self.request.GET['maximo'] != "":
            try:
                if query == None:
                    query = Q(price__lte=int(float(self.request.GET['maximo'])))
                else:
                    query = query & Q(price__lte=int(float(self.request.GET['maximo'])))
            except:
                pass


        if ('minimo' in self.request.GET) and self.request.GET['minimo'] != "":
            try:
                if query == None:
                    query = Q(price__gte=int(float(self.request.GET['minimo'])))
                else:
                    query = query & Q(price__gte=int(float(self.request.GET['minimo'])))
            except:
                pass


        if query is not None:
            productos = Design.objects.filter(query)
        else:
            productos = Design.objects.all()
        return productos
    
    def get_context_data(self, **kwargs):
        context = super(ListaProductos, self).get_context_data(**kwargs)
        context['maximo'] = Design.objects.all().aggregate(Max('price'))['price__max']
        context['minimo'] = Design.objects.all().aggregate(Min('price'))['price__min']
        return context
            
class DetalleProducto(DetailView):
    template_name="catalog/detalleProducto.html"
    model=Design

class ComentarioProducto(CreateView):
    model=Comentario
    fields=("comentario","usuario","producto")

    def get_success_url(self):
        return "/catalog/detalleProductos/{}/".format(self.object.producto.pk)

class AniadirCarrito(LoginRequiredMixin, CreateView):
    model = CarritoCompras
    fields = ("usuario","producto","price")
    success_url = reverse_lazy("listaProductos")
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        print(form.errors)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class EliminarCarrito(LoginRequiredMixin,DeleteView):
    queryset = CarritoCompras.objects.filter(comprado=False)
    model = CarritoCompras
    success_url = reverse_lazy('listarCarrito')
    login_url = 'login'

class ListarCarrito(LoginRequiredMixin,ListView):
    template_name = 'catalog/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=False)
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(ListarCarrito, self).get_context_data(**kwargs)
        context['tab'] = 'sincomprar'
        return context

class ListarCarritoPendientes(LoginRequiredMixin,ListView):
    template_name = 'catalog/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=True)
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoPendientes, self).get_context_data(**kwargs)
        context['tab'] = 'pendientes'
        return context

class ListarCarritoFinalizadas(LoginRequiredMixin,ListView):
    template_name = 'catalog/carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=True,pendiente=False)
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoFinalizadas, self).get_context_data(**kwargs)
        context['tab'] = 'finalizadas'
        return context

class DetallePago(TemplateView):
    template_name="catalog/detalle_pago.html"