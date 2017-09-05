from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import View
from forms import *
import json
from models import *

# Create your views here.
def docente(request):
    if "cedula" in request.session:
        cedula = request.session["cedula"]
        usuario = Usuario.objects.get(cedula=cedula)
        
        return render(request, "Proyeccion/docente.html", {'nombre':usuario.nombre})
    else:
        return HttpResponseRedirect("/")
    
def proyectos(request):
    if "cedula" in request.session:
        cedula = request.session["cedula"]
        usuario = Usuario.objects.get(cedula=cedula)     
        return render(request, "Proyeccion/proyectos.html", {'nombre':usuario.nombre})
    else:
        return HttpResponseRedirect("/")
    
def cerrarSession(request):
    try:
        del request.session['cedula']
    except KeyError:
        pass
    return HttpResponseRedirect("/")

class Logear(View):
    def get(self, request, * args, ** kwargs):
        return render(request, 'inicio/login.html', {})
    def post(self, request, * args, ** kwargs):
        usuario = request.POST['usuario']
        clave = request.POST['clave']    
        try:  
            user = Usuario.objects.get(cedula=usuario, clave=clave)
            response_data = {}
            response_data['respuesta'] = 'existe'  
            request.session['cedula'] = user.cedula
            request.session['identificador'] = user.id
        except Usuario.DoesNotExist:
            response_data = {}
            response_data['respuesta'] = 'noExiste'          
        return HttpResponse(json.dumps(response_data), content_type='application/json')

class ConsultarProyectos(View):
    def get(self, request, * args, ** kwargs):
        informacion_list = InformacionDescriptiva.objects.filter(coordinador_id=request.session['identificador'])
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            nombre = usuario.nombre
            return render(request, "Proyeccion/consultarProyectos.html", {'informacion_list':informacion_list, 'nombre':nombre})
        else:
            return HttpResponseRedirect("/")
    
class CrearProyecto(CreateView):
    template_name = 'Proyeccion/crearProyecto.html'
    model = InformacionDescriptiva
    form_class = InformacionDescriptivaForm
    nombre = ""
    success_url = reverse_lazy('ConsultarProyectos')
    def get(self, request, * args, ** kwargs):
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            self.nombre = usuario.nombre
            return super(CrearProyecto, self).get(request, * args, ** kwargs)
        else:
            return HttpResponseRedirect("/")
    
    def form_valid(self, form):
        fechap = form.instance.fecha
        fechainiciop = form.instance.fecha_inicio
        fechafinalp = form.instance.fecha_final
        if (fechap.month < fechainiciop.month):
            if (fechafinalp.month > fechainiciop.month or (fechafinalp.month == fechainiciop.month and fechafinalp.day >= fechainiciop.day)):
                print "hola1"
                return super(CrearProyecto, self).form_valid(form)
            else:
                print "hola2"
                mensaje = "La fecha de inicio debe ser menor a la fecha final del proyecto"
                form.add_error('fecha', mensaje)
                return super(CrearProyecto, self).form_invalid(form)
        else:
            mensaje = "La fecha  registro de proyecto debe ser menor a la fecha de inicio del proyecto"
            form.add_error('fecha', mensaje)
            return super(CrearProyecto, self).form_invalid(form)
    
    def get_context_data(self, ** kwargs):
	context = super(CrearProyecto, self).get_context_data( ** kwargs)
        context['nombre'] = self.nombre
        return context
    
class ModificarProyecto(UpdateView):
    template_name = 'Proyeccion/modificarProyecto.html'
    model = InformacionDescriptiva
    form_class = InformacionDescriptivaForm
    nombre = ""
    success_url = reverse_lazy('ConsultarProyectos')
    def get(self, request, * args, ** kwargs):
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            self.nombre = usuario.nombre
            return super(ModificarProyecto, self).get(request, * args, ** kwargs)
        else:
            return HttpResponseRedirect("/")
        
    def form_valid(self, form):
        fechap = form.instance.fecha
        fechainiciop = form.instance.fecha_inicio
        fechafinalp = form.instance.fecha_final
        if (fechap.month < fechainiciop.month):
            if (fechafinalp.month > fechainiciop.month or (fechafinalp.month == fechainiciop.month and fechafinalp.day >= fechainiciop.day)):
                return super(ModificarProyecto, self).form_valid(form)
            else:
                mensaje = "La fecha de inicio debe ser menor a la fecha final del proyecto"
                form.add_error('fecha', mensaje)
                return super(ModificarProyecto, self).form_invalid(form)
        else:
            mensaje = "La fecha  registro de proyecto debe ser menor a la fecha de inicio del proyecto"
            form.add_error('fecha', mensaje)
            return super(ModificarProyecto, self).form_invalid(form)
        
        
    def get_context_data(self, ** kwargs):
	context = super(ModificarProyecto, self).get_context_data( ** kwargs)
        context['nombre'] = self.nombre
        return context
    
class EliminarProyecto(DeleteView):
    template_name = 'Proyeccion/eliminarProyecto.html'
    model = InformacionDescriptiva
    success_url = reverse_lazy('ConsultarProyectos')
    
class ConsultarRecursoEstudiante(View):
    def get(self, request, * args, ** kwargs):
        informacion_list = RecursoEstudiante.objects.filter(proyecto_id=request.session['identificador'])
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            nombre = usuario.nombre
            informacionDescriptivaId = kwargs["pk"]
            informacion = InformacionDescriptiva.objects.get(id=informacionDescriptivaId)
            return render(request, "Proyeccion/consultarRecursoEstudiante.html", {'informacion':informacion, 'informacion_list':informacion_list, 'nombre':nombre})
        else:
            return HttpResponseRedirect("/")
        
class ConsultarRecursoDocente(View):
    def get(self, request, * args, ** kwargs):
        informacion_list = RecursoDocente.objects.filter(proyecto_id=request.session['identificador'])
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            nombre = usuario.nombre
            informacionDescriptivaId = kwargs["pk"]
            informacion = InformacionDescriptiva.objects.get(id=informacionDescriptivaId)
            return render(request, "Proyeccion/consultarRecursoDocente.html", {'informacion':informacion, 'informacion_list':informacion_list, 'nombre':nombre})
        else:
            return HttpResponseRedirect("/")
        
class CrearRecursoDocente(CreateView):
    template_name = 'Proyeccion/crearRecursoDocente.html'
    model = RecursoDocente
    form_class = RecursoDocenteForm
    nombre = ""
    success_url = reverse_lazy('ConsultarProyectos')
    
    def get(self, request, * args, ** kwargs):
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            self.nombre = usuario.nombre
            return super(CrearRecursoDocente, self).get(request, * args, ** kwargs)
        else:
            return HttpResponseRedirect("/")
    
    def form_valid(self, form):
        fechainiciop = form.instance.fecha_inicio
        fechafinalp = form.instance.fecha_final
        if (fechafinalp.month > fechainiciop.month or (fechafinalp.month == fechainiciop.month and fechafinalp.day >= fechainiciop.day)):
            proyecto = Proyecto.objects.get(id=self.kwargs["pk"])
            form.instance.proyecto_id = proyecto
            return super(CrearRecursoDocente, self).form_valid(form)    
        else:
            mensaje = "La fecha de inicio debe ser menor a la fecha final"
            form.add_error('fecha_inicio', mensaje)
            return super(CrearRecursoDocente, self).form_invalid(form)
        
    
    def get_context_data(self, ** kwargs):
	context = super(CrearRecursoDocente, self).get_context_data(** kwargs)
        context['nombre'] = self.nombre
        return context
    def get_success_url(self):
        return reverse('ConsultarRecursoDocente', kwargs={'pk':self.kwargs['pk']})
    
class ModificarRecursoDocente(UpdateView):
    template_name = 'Proyeccion/modificarRecursoDocente.html'
    model = RecursoDocente
    form_class = ModificarRecursoDocenteForm
    nombre = ""
    
    def get(self, request, * args, ** kwargs):
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            self.nombre = usuario.nombre
            return super(ModificarRecursoDocente, self).get(request, * args, ** kwargs)
        else:
            return HttpResponseRedirect("/")
        
    def get_context_data(self, ** kwargs):
	context = super(ModificarRecursoDocente, self).get_context_data( ** kwargs)
        context['nombre'] = self.nombre
        return context
    def get_success_url(self):
        proyecto = RecursoDocente.objects.get(id=self.kwargs['pk'])
        return reverse('ConsultarRecursoDocente', kwargs={'pk': proyecto.proyecto_id})

class EliminarRecursoDocente(DeleteView):
    template_name = 'Proyeccion/eliminarRecursoDocente.html'
    model = RecursoDocente
    
    def get_sucess_url(self):
        proyecto = RecursoDocente.objects.get(id=self.kwargs['pk'])
        return reverse('ConsultarRecursoDocete', kwargs={'pk': proyecto.proyecto_id})
    
class CrearRecursoEstudiante(CreateView):
    template_name = 'Proyeccion/crearRecursoEstudiante.html'
    model = RecursoEstudiante
    form_class = RecursoEstudianteForm
    nombre = ""
    
    def get(self, request, * args, ** kwargs):
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            self.nombre = usuario.nombre
            return super(CrearRecursoEstudiante, self).get(request, * args, ** kwargs)
        else:
            return HttpResponseRedirect("/")
        
    def form_valid(self, form):
        fechainiciop = form.instance.fecha_inicio
        fechafinalp = form.instance.fecha_final
        if (fechafinalp.month > fechainiciop.month or (fechafinalp.month == fechainiciop.month and fechafinalp.day >= fechainiciop.day)):
            proyecto = Proyecto.objects.get(id=self.kwargs["pk"])
            form.instance.proyecto_id = proyecto
            return super(CrearRecursoEstudiante, self).form_valid(form)    
        else:
            mensaje = "La fecha de inicio debe ser menor a la fecha final"
            form.add_error('fecha_inicio', mensaje)
            return super(CrearRecursoEstudiante, self).form_invalid(form)
    
    def get_context_data(self, ** kwargs):
	context = super(CrearRecursoEstudiante, self).get_context_data(** kwargs)
        context['nombre'] = self.nombre
        return context
    
    def get_success_url(self):
        return reverse('ConsultarRecursoEstudiante', kwargs={'pk': self.kwargs['pk']})

class ModificarRecursoEstudiante(UpdateView):
    template_name = 'Proyeccion/modificarRecursoEstudiante.html'
    model = RecursoEstudiante
    form_class = ModificarRecursoEstudianteForm
    nombre = ""
    def get(self, request, * args, ** kwargs):
        if "cedula" in request.session:
            cedula = request.session["cedula"]
            usuario = Usuario.objects.get(cedula=cedula) 
            self.nombre = usuario.nombre
            return super(ModificarRecursoEstudiante, self).get(request, * args, ** kwargs)
        else:
            return HttpResponseRedirect("/")
    def get_context_data(self, ** kwargs):
	context = super(ModificarRecursoEstudiante, self).get_context_data( ** kwargs)
        context['nombre'] = self.nombre
        return context
    def get_success_url(self):
        proyecto = RecursoEstudiante.objects.get(id=self.kwargs['pk'])
        return reverse('ConsultarRecursoEstudiante', kwargs={'pk': proyecto.proyecto_id})
    
class EliminarRecursoEstudiante(DeleteView):
    template_name = 'Proyeccion/eliminarRecursoEstudiante.html'
    model = RecursoEstudiante
    
    def get_sucess_url(self):
        proyecto = RecursoEstudiante.objects.get(id=self.kwargs['pk'])
        return reverse('ConsultarRecursoEstudiante', kwargs={'pk': proyecto.proyecto_id})
    
