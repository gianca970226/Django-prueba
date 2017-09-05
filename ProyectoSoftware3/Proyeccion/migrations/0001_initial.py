# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200, null=True)),
                ('telefono', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_hora', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200, null=True)),
                ('telefono', models.CharField(max_length=200, null=True)),
                ('decano_id', models.ForeignKey(to='Proyeccion.Docente')),
            ],
        ),
        migrations.CreateModel(
            name='InformacionDescriptiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('codigo', models.CharField(max_length=200)),
                ('numero_convenio', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('problema', models.CharField(max_length=200)),
                ('justificacion', models.CharField(max_length=200, null=True)),
                ('objetivo_general', models.CharField(max_length=200)),
                ('impacto', models.CharField(max_length=200, null=True)),
                ('poblacion', models.CharField(max_length=200, null=True)),
                ('metodologia', models.CharField(max_length=200, null=True)),
                ('coordinador_id', models.ForeignKey(to='Proyeccion.Docente')),
                ('departamento_id', models.ForeignKey(to='Proyeccion.Departamento')),
                ('facultad_id', models.ForeignKey(to='Proyeccion.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('relevancia', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ObjetivoEspelcifico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objetivo', models.CharField(max_length=200, null=True)),
                ('informacion_descriptiva_id', models.ForeignKey(to='Proyeccion.InformacionDescriptiva')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=200)),
                ('clave', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VinculacionDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='informaciondescriptiva',
            name='modalidad_id',
            field=models.ForeignKey(to='Proyeccion.Modalidad'),
        ),
        migrations.AddField(
            model_name='docente',
            name='usuario_id',
            field=models.ForeignKey(to='Proyeccion.Usuario'),
        ),
        migrations.AddField(
            model_name='docente',
            name='vinculacion_id',
            field=models.ForeignKey(to='Proyeccion.VinculacionDocente'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='director_id',
            field=models.ForeignKey(to='Proyeccion.Docente'),
        ),
    ]
