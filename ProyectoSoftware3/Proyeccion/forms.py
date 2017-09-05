# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from django import forms
from models import *
class InformacionDescriptivaForm(forms.ModelForm):
    class Meta:
        model = InformacionDescriptiva

        fields = [
            'fecha',
            'codigo',
            'numero_convenio',
            'titulo',
            'coordinador_id',
            'departamento_id',
            'facultad_id',
            'fecha_inicio',
            'fecha_final',
            'modalidad_id',
            'problema',
            'justificacion',
            'objetivo_general',
            'objetivos_especificos',
            'impacto',
            'poblacion',
            'metodologia',
        ]
        labels = {
            'fecha':'FECHA',
            'codigo':'CODIGO',
            'numero_convenio':'CONVENIO',
            'titulo':'TITULO',
            'coordinador_id':'COORDINADOR',
            'departamento_id':'DEPARTAMENTO',
            'facultad_id':'FACULTAD',
            'fecha_inicio':'FECHA INCIO',
            'fecha_final':'FECHA FINAL',
            'modalidad_id':'MODALIDAD',
            'problema':'PROBLEMA',
            'justificacion':'JUSTIFICACION',
            'objetivo_general':'OBJETIVO GENERAL',
            'objetivos_especificos':'OBJETIVOS ESPECIFICOS',
            'impacto':'IMPACTO',
            'poblacion':'POBLACION',
            'metodologia':'METODOLOGIA',
		
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'numero_convenio': forms.TextInput(attrs={'class':'form-control'}),
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'coordinador_id': forms.Select(attrs={'class':'form-control'}),
            'departamento_id': forms.Select(attrs={'class':'form-control'}),
            'facultad_id': forms.Select(attrs={'class':'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fecha_final': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'modalidad_id': forms.Select(attrs={'class':'form-control'}),
            'objetivo_general': forms.Textarea(attrs={'class':'form-control'}),
            'objetivos_especificos': forms.Textarea(attrs={'class':'form-control'}),
            'impacto': forms.Textarea(attrs={'class':'form-control'}),
            'poblacion': forms.Textarea(attrs={'class':'form-control'}),
            'justificacion': forms.Textarea(attrs={'class':'form-control'}),
            'metodologia': forms.Textarea(attrs={'class':'form-control'}),
            'problema': forms.Textarea(attrs={'class':'form-control'}),
        }
        
        
class RecursoDocenteForm(forms.ModelForm):
    class Meta:
        model = RecursoDocente
        exclude = ['proyecto_id']

        fields = [
            'docente_id',
            'numero_horas_semana',
            'fecha_inicio',
            'fecha_final',
            'tipo_financiacion',
#            'proyecto_id'
        ]
        labels = {
            'docente_id':'DOCENTE',
            'numero_horas_semana':'NUMERO HORAS SEMANA',
            'fecha_inicio':'FECHA INICIO',
            'fecha_final':'FECHA FINAL',
            'tipo_financiacion':'TIPO DE FINANCIACION',
#            'proyecto_id': 'PROYECTO',
        }
        widgets = {
            'docente_id': forms.Select(attrs={'class':'form-control'}),
            'numero_horas_semana': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fecha_final': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'tipo_financiacion': forms.TextInput(attrs={'class':'form-control'}),
#            'proyecto_id': forms.TextInput(attrs={'class':'form-control'}),
        }

class RecursoEstudianteForm(forms.ModelForm):
    class Meta:
        model = RecursoEstudiante
        exclude = ['proyecto_id']
        
        fields = [
            'nombre',
            'codigo',
            'programa_id',
            'semestre',
            'numero_horas_semana',
            'fecha_inicio',
            'fecha_final',
#            'proyecto_id'
        ]
        labels = {
            'nombre':'NOMBRE',
            'codigo':'CODIGO',
            'programa_id':'PROGRAMA',
            'semestre':'SEMESTRE',
            'numero_horas_semana':'NUMERO HORAS SEMANA',
            'fecha_inicio':'FECHA INICIO',
            'fecha_final':'FECHA FINAL',
#            'proyecto_id': 'PROYECTO',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'programa_id':forms.Select(attrs={'class':'form-control'}),
            'semestre': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'numero_horas_semana': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fecha_final': forms.DateInput(attrs={'class':'form-control','type':'date'}),
#            'proyecto_id': forms.TextInput(attrs={'class':'form-control'}),
        }
    
class ModificarRecursoEstudianteForm(forms.ModelForm):
    class Meta:
        model = RecursoEstudiante
        fields = [
            'nombre',
            'codigo',
            'programa_id',
            'semestre',
            'numero_horas_semana',
            'fecha_inicio',
            'fecha_final',
            'proyecto_id',
        ]
        labels = {
            'nombre':'NOMBRE',
            'codigo':'CODIGO',
            'programa_id':'PROGRAMA',
            'semestre':'SEMESTRE',
            'numero_horas_semana':'NUM HORAS SEMANALES',
            'fecha_inicio':'FECHA INICIAL',
            'fecha_final':'FECHA FINAL',
            'proyecto_id':'NOMBRE PROYECTO ',
		
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'programa_id': forms.Select(attrs={'class':'form-control'}),
            'semestre': forms.TextInput(attrs={'class':'form-control'}),
            'numero_horas_semana': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fecha_final': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'proyecto_id': forms.Select(attrs={'class':'form-control'}),
        }
 
    
class ModificarRecursoDocenteForm(forms.ModelForm):
    class Meta:
        model = RecursoDocente
        fields = [
            'docente_id',
            'numero_horas_semana',
            'fecha_inicio',
            'fecha_final',
            'tipo_financiacion',
            'proyecto_id',
        ]
        labels = {
            'docente_id':'DOCENTE',
            'numero_horas_semana':'NUM HORAS SEMANALES',
            'fecha_inicio':'FECHA INICIO',
            'fecha_final':'FECHA FINAL',
            'tipo_financiacion':'FINANCIACION',
            'proyecto_id':'PROYECTO',
            	
        }
        widgets = {
            'docente_id': forms.Select(attrs={'class':'form-control'}),
            'numero_horas_semana': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fecha_final': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'tipo_financiacion': forms.TextInput(attrs={'class':'form-control'}),
            'proyecto_id': forms.Select(attrs={'class':'form-control'}),
        }

