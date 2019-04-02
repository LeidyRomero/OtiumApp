# Generated by Django 2.1.7 on 2019-04-02 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ubicacion', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salario', models.IntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('jornada', models.CharField(max_length=255)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombre_empresa', to='ofertas.Empresa')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubicacion_empresa', to='ofertas.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requerimiento', models.TextField()),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ofertas.Oferta')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='empresa',
            unique_together={('nombre', 'ubicacion')},
        ),
        migrations.AlterUniqueTogether(
            name='requerimiento',
            unique_together={('oferta', 'requerimiento')},
        ),
        migrations.AlterUniqueTogether(
            name='oferta',
            unique_together={('titulo', 'nombre')},
        ),
    ]
