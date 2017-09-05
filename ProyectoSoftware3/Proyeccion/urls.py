
from django.conf.urls import url
from views import *
urlpatterns = [
    #Mapa de rutas de la aplicacion de Proyeccion 
    url(r'^Docente/$', docente),
    url(r'^Proyectos/$', ConsultarProyectos.as_view(), name='ConsultarProyectos'),
    url(r'^CrearProyecto/$', CrearProyecto.as_view()),
    url(r'^RecursoEstudiante/(?P<pk>\d+)$', ConsultarRecursoEstudiante.as_view(),name='ConsultarRecursoEstudiante'),
    url(r'^RecursoDocente/(?P<pk>\d+)$', ConsultarRecursoDocente.as_view(),name='ConsultarRecursoDocente'),
    url(r'^CrearRecursoDocente/(?P<pk>\d+)$', CrearRecursoDocente.as_view()),
    url(r'^CrearRecursoEstudiante/(?P<pk>\d+)$', CrearRecursoEstudiante.as_view()),
    url(r'^ModificarProyecto/(?P<pk>\d+)$', ModificarProyecto.as_view()),
    url(r'^EliminarProyecto/(?P<pk>\d+)$', EliminarProyecto.as_view()),
    url(r'^ModificarRecursoEstudiante/(?P<pk>\d+)$', ModificarRecursoEstudiante.as_view()),
    url(r'^ModificarRecursoDocente/(?P<pk>\d+)$', ModificarRecursoDocente.as_view()),
    url(r'^EliminarRecursoEstudiante/(?P<pk>\d+)$', EliminarRecursoEstudiante.as_view()),
    url(r'^EliminarRecursoDocente/(?P<pk>\d+)$', EliminarRecursoDocente.as_view()),
    url(r'^CerrarSession/$', cerrarSession),
]

