# Generated by Django 2.1.7 on 2019-04-03 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HabilidadBlanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('formulario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habilidad_formulario', to='formulario.Formulario')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('formulario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materia_formulario', to='formulario.Formulario')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='materia',
            unique_together={('nombre', 'formulario')},
        ),
        migrations.AlterUniqueTogether(
            name='habilidadblanda',
            unique_together={('nombre', 'formulario')},
        ),
    ]
