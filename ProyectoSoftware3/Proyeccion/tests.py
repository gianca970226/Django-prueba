from django.test import TestCase
from models import *
from django.core.exceptions import ValidationError

# Create your tests here.

class UsuarioTest(TestCase):
    def setUp(self):
        Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
    def test_loginValidate(self):
        usuario = Usuario(nombre="GIAN", cedula="1053855850", clave="12345")
        try:  
            usuarioLogin = Usuario.objects.get(cedula=usuario.cedula, clave=usuario.clave)
            self.assertTrue(True)
        except:             
            self.assertTrue(False)
            
    def test_loginInvalidate(self):
        usuario = Usuario(nombre="GIAN", cedula="1053855850", clave="123456")
        try:  
            usuarioLogin = Usuario.objects.get(cedula=usuario.cedula, clave=usuario.clave)
            self.assertTrue(False)
        except:             
            self.assertTrue(True)   
            
class RegisterProjectTest(TestCase): 
    def setUp(self):
        Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
    def test_registerProjectValidate(self):
      
        docente= Docente.objects.get(valor_hora=35000)
        departamento= Departamento.objects.get(nombre="SALUD INTERNA")
        facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
        modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
        try:     
            proyecto=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION DEL PROYECTO", metodologia="METODOLOGIA PROYECTO")
            proyecto.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_registerProjectInvalidateEmptyFacultad(self):
        docente= Docente.objects.get(valor_hora=35000)
        departamento= Departamento.objects.get(nombre="SALUD INTERNA")
        facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
        modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
        
        try:     
            proyecto=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=docente, departamento_id=departamento, facultad_id=None,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
            proyecto.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
            
    def test_registerProjectInvalidateEmptyDocente(self):
        departamento= Departamento.objects.get(nombre="SALUD INTERNA")
        facultad= Facultad.objects.get(nombre="CIENCIAS PARA LA SALUD")
        modalidad= Modalidad.objects.get(nombre="SEMINARIO",)
        
        try:     
            proyecto=InformacionDescriptiva(fecha="2016-05-05", codigo="VPU-000", 
            numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
            coordinador_id=None, departamento_id=departamento, facultad_id=facultad,
            fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
            problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
            objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
            impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
            proyecto.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
class updateProjectTest(TestCase):
    
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
        
    def test_updateProjectValidate(self):
        try:
            proyecto = InformacionDescriptiva.objects.get(codigo="VPU-000")
            proyecto.titulo="CONGRESO DE MEDICINA"
            proyecto.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_updateProjectInvalidateEmptyTitulo(self):
        try:
            proyecto = InformacionDescriptiva.objects.get(codigo="VPU-000")
            proyecto.titulo=None
            proyecto.save()
            self.assertTrue(False) 
        except:       
            self.assertTrue(True)
    
    def test_updateProjectInvalidateEmptyDepartamento(self):
        try:
            proyecto = InformacionDescriptiva.objects.get(codigo="VPU-000")
            proyecto.departamento=None
            proyecto.save()
            self.assertTrue(False) 
            
        except:
            self.assertTrue(True)
        

class DeleteProjectTest(TestCase): 
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
        
            
    def test_DeleteProjectValidate(self):
        try:     
            proyecto=InformacionDescriptiva.objects.get(codigo="VPU-000")
            proyecto.delete()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
    
    def test_DeleteProjectInvalidate(self):
        try:     
            proyecto=InformacionDescriptiva.objects.get(codigo="VPU-001")
            proyecto.delete()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
    
            
class RegisterTeachingTest(TestCase): 
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        informacion=InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
        
        Proyecto.objects.create(activo=True, informacion_descriptiva_id=informacion)
        
        
    def test_registerTeachingValidate(self):
        try:
            docente= Docente.objects.get(valor_hora=35000)
            proyecto=Proyecto.objects.all()
            recursoDocente=RecursoDocente(numero_horas_semana=4, fecha_inicio="2016-07-08", fecha_final="2016-07-09", tipo_financiacion="RECURRENTE", docente_id=docente, proyecto_id=proyecto[0])
            recursoDocente.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_registerTeachingInvalidateEmptyNumeroHoras(self):
        docente= Docente.objects.get(valor_hora=35000)
        proyecto= Proyecto.objects.all()
        
        try:     
            recursoDocente=RecursoDocente(numero_horas_semana=None, fecha_inicio="2016-07-08", fecha_final="2016-07-09", tipo_financiacion="RECURRENTE", docente_id=docente, proyecto_id=proyecto[0])
            recursoDocente.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
            
    def test_registerTeachingInvalidateEmptyFechaFinal(self):
        docente= Docente.objects.get(valor_hora=35000)
        proyecto= Proyecto.objects.all()
        try:     
            recursoDocente=RecursoDocente(numero_horas_semana=4, fecha_inicio="2016-07-12", fecha_final=None, tipo_financiacion="RECURRENTE", docente_id=docente, proyecto_id=proyecto[0])
            recursoDocente.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
class updateTeachingTest(TestCase):
    
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        
        informacion=InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
        
        proyecto=Proyecto.objects.create(activo=True, informacion_descriptiva_id=informacion)
        RecursoDocente.objects.create(numero_horas_semana=2, fecha_inicio="2016-07-12", fecha_final="2016-07-18", tipo_financiacion="RECURRENTE", docente_id=docente, proyecto_id=proyecto)
        
    def test_updateTeachingValidate(self):
        try:
            recursoDocente=RecursoDocente.objects.get(numero_horas_semana=2)
            recursoDocente.numero_horas_semana=10
            recursoDocente.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_updateTeachingInvalidateEmptyNumeroHorasSemana(self):
        try:
            recursoDocente=RecursoDocente.objects.get(numero_horas_semana=10)
            recursoDocente.numero_horas_semana=None
            recursoDocente.save()
            self.assertTrue(False) 
        except:       
            self.assertTrue(True)
    
    def test_updateTeachingInvalidateEmptyTipoFinanciacion(self):
        try:
            recursoDocente=RecursoDocente.objects.get(numero_horas_semana=10)
            recursoDocente.tipo_financiacion=None
            recursoDocente.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
class RegisterStudentTest(TestCase): 
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        facultad2=Facultad.objects.create(nombre="INGENIERIAS", decano_id=docente,
        correo="INGENIERIAS@UCALDAS.EDU.CO", telefono="8750584")
        Programa.objects.create(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION", director_id=docente, facultad_id=facultad2)
        
        informacion=InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
        
        Proyecto.objects.create(activo=True, informacion_descriptiva_id=informacion)
        
    def test_registerStudentValidate(self):
        try:
            programa=Programa.objects.get(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION")
            proyecto=Proyecto.objects.all()
            recursoEstudiante=RecursoEstudiante(nombre="JULIAN",codigo="1701313530",semestre=6,numero_horas_semana=5, fecha_inicio="2016-07-12", fecha_final="2016-07-18", programa_id=programa, proyecto_id=proyecto[0])
            recursoEstudiante.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_registerStudentInvalidateEmptyCodigo(self):
        programa=Programa.objects.get(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION")
        proyecto= Proyecto.objects.all()
        try:     
            recursoEstudiante=RecursoEstudiante(nombre="JULIAN",codigo=None,semestre=6,numero_horas_semana=5, fecha_inicio="2016-07-12", fecha_final="2016-07-18", programada_id=programa, proyecto_id=proyecto[0])
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
            
    def test_registerStudentInvalidateEmptyNumeroHorasSemana(self):
        programa= Programa.objects.get(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION")
        proyecto= Proyecto.objects.all()
        try:     
            recursoEstudiante=RecursoEstudiante(nombre="JULIAN",codigo="1701313530",semestre=6,numero_horas_semana=None, fecha_inicio="2016-07-12", fecha_final="2016-07-18", programada_id=programa, proyecto_id=proyecto[0])
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
class updateStudentTest(TestCase):
    
    def setUp(self):
        modalidad=Modalidad.objects.create(nombre="SEMINARIO", relevancia=5)
        usuario=Usuario.objects.create(nombre="GIAN", cedula="1053855850", clave="12345")
        vinculacion=VinculacionDocente.objects.create(tipo="DOCENTE DE PLANTA")
        docente=Docente.objects.create(valor_hora=35000, vinculacion_id=vinculacion, usuario_id=usuario)
        departamento=departamento=Departamento.objects.create(nombre="SALUD INTERNA", director_id=docente, 
        correo="SALUDINTERNA@UCALDAS.EDU.CO", telefono="8595231")
        facultad=Facultad.objects.create(nombre="CIENCIAS PARA LA SALUD", decano_id=docente,
        correo="SAUD@UCALDAS.EDU.CO", telefono="8754522")
        facultad2=Facultad.objects.create(nombre="INGENIERIAS", decano_id=docente,
        correo="INGENIERIAS@UCALDAS.EDU.CO", telefono="8750584")
        programa=Programa.objects.create(nombre="INGENIERIA DE SISTEMAS Y COMPUTACION", director_id=docente, facultad_id=facultad2)
        
        informacion=InformacionDescriptiva.objects.create(fecha="2016-05-05", codigo="VPU-000", 
        numero_convenio="UNIVERSIDAD DE CALDAS", titulo="SEMINARIO DE MEDICINA", 
        coordinador_id=docente, departamento_id=departamento, facultad_id=facultad,
        fecha_inicio="2016-07-07", fecha_final="2016-08-08",modalidad_id=modalidad, 
        problema="PROBLEMA PROYECTO", justificacion="JUSTIFICACION PROYECTO", 
        objetivo_general="OBJETIVO PROYECTO", objetivos_especificos="OBJETIVOS ESPECIFICOS PROYECTO", 
        impacto="IMPACTO PROYECTO", poblacion="POBLACION AL PROYECTO", metodologia="METODOLOGIA PROYECTO")
        
        proyecto=Proyecto.objects.create(activo=True, informacion_descriptiva_id=informacion)
        RecursoEstudiante.objects.create(nombre="JULIAN",codigo="1701313530",semestre=6,numero_horas_semana=5, fecha_inicio="2016-07-12", fecha_final="2016-07-18", programa_id=programa, proyecto_id=proyecto)
        
    def test_updateStudentValidate(self):
        try:
            recursoEstudiante=RecursoEstudiante.objects.get(codigo="1701313530")
            print recursoEstudiante.nombre
            print recursoEstudiante.codigo
            recursoEstudiante.nombre="CRISTIAN"
            recursoEstudiante.numero_horas_semana=10
            recursoEstudiante.save()
            self.assertTrue(True) 
        except:
            self.assertTrue(False)
            
    def test_updateTeachingInvalidateEmptyTipoCodigo(self):
        try:
            recursoEstudiante=RecursoEstudiante.objects.get(codigo="1701313530")
            recursoEstudiante.codigo=None
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:
            self.assertTrue(True)
            
    def test_updateStudentInvalidateEmptyNumeroHorasSemana(self):
        try:
            recursoEstudiante=RecursoEstudiante.objects.get(codigo="1701313530")
            recursoEstudiante.numero_horas_semana=None
            recursoEstudiante.save()
            self.assertTrue(False) 
        except:       
            self.assertTrue(True)    