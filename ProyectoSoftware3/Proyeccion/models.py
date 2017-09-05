from __future__ import unicode_literals

from django.db import models

# Create your models here.
    
class Usuario(models.Model):
    nombre=models.CharField(max_length=200)
    cedula=models.CharField(max_length=200)
    clave=models.CharField(max_length=200)
    def __str__(self):
        return '%s'%(self.nombre)
    
class VinculacionDocente(models.Model):
    tipo=models.CharField(max_length=200)
    def __str__(self):
        return '%s'%(self.tipo)

class Docente(models.Model):
    valor_hora=models.IntegerField()
    vinculacion_id=models.ForeignKey(VinculacionDocente, on_delete=models.CASCADE)
    usuario_id=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return '%s'%(self.usuario_id)

class Departamento(models.Model):
    nombre=models.CharField(max_length=200)
    director_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    correo=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    def __str__(self):
        return '%s'%(self.nombre)
    
class Facultad(models.Model):
    nombre=models.CharField(max_length=200)
    decano_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    correo=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    def __str__(self):
        return '%s'%(self.nombre)
    
class Modalidad(models.Model):
    nombre=models.CharField(max_length=200)
    relevancia=models.IntegerField(null=True)
    def __str__(self):
        return '%s'%(self.nombre)
    
class InformacionDescriptiva(models.Model):
    
    fecha=models.DateField(null=False, blank=False)
    codigo=models.CharField(null=False, blank=False,max_length=200)
    numero_convenio=models.CharField(null=False, blank=False,max_length=200)
    titulo=models.CharField(null=False, blank=False,max_length=400)
    coordinador_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    departamento_id=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    facultad_id=models.ForeignKey(Facultad, on_delete=models.CASCADE)
    fecha_inicio=models.DateField(null=False, blank=False)
    fecha_final=models.DateField(null=False, blank=False)
    modalidad_id=models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    problema=models.TextField(null=False, blank=False)
    justificacion=models.TextField(null=False, blank=False)
    objetivo_general=models.TextField(null=False, blank=False)
    objetivos_especificos=models.TextField(null=False, blank=False)
    impacto=models.TextField(null=False, blank=False)
    poblacion=models.TextField(null=False, blank=False)
    metodologia=models.TextField(null=False, blank=False)
    def __str__(self):
        return '%s'%(self.id)

class Proyecto(models.Model):
    activo=models.BooleanField(blank=True)
    informacion_descriptiva_id=models.ForeignKey(InformacionDescriptiva, on_delete=models.CASCADE)
    def __str__(self):
        return '%s'%(self.informacion_descriptiva_id)
    
class RecursoDocente(models.Model):
    docente_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    numero_horas_semana=models.IntegerField(null=False, blank=False)
    fecha_inicio=models.DateField(null=False, blank=False)
    fecha_final=models.DateField(null=False, blank=False)
    tipo_financiacion=models.CharField(null=False, blank=False, max_length=200)
    proyecto_id=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s'%(self.docente_id)

class Programa(models.Model):
    nombre=models.CharField(null=False, blank=False, max_length=200)
    director_id=models.ForeignKey(Docente, on_delete=models.CASCADE)
    facultad_id=models.ForeignKey(Facultad, on_delete=models.CASCADE)
    def __str__(self):
        return '%s'%(self.nombre)
    
class RecursoEstudiante(models.Model):
    nombre=models.CharField(null=False, blank=False, max_length=200)
    codigo=models.CharField(null=False, blank=False, max_length=200)
    programa_id=models.ForeignKey(Programa, on_delete=models.CASCADE)
    semestre=models.IntegerField(null=True, blank=False)
    numero_horas_semana=models.IntegerField(null=False, blank=False)
    fecha_inicio=models.DateField(null=False, blank=False)
    fecha_final=models.DateField(null=False, blank=False)
    proyecto_id=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    def __str__(self):
        return '%s'%(self.nombre) 