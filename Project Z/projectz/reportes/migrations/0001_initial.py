# Generated by Django 4.2.4 on 2023-08-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearReporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Sin Nombrar', max_length=300, verbose_name='Título del reporte')),
                ('accion', models.CharField(default='Sin Especificar', max_length=300, verbose_name='Reportar problema/solicitud de información')),
                ('categoria', models.CharField(default='Sin Especificar', max_length=300, verbose_name='Categoría')),
                ('estado', models.CharField(default='Sin Especificar', max_length=300, verbose_name='Estado')),
                ('ciudad', models.CharField(default='Sin Especificar', max_length=300, verbose_name='Ciudad')),
                ('cp', models.IntegerField(default=0, verbose_name='Código Postal')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('descripcion', models.CharField(default='Sin Especificar', max_length=300, verbose_name='Descripción')),
            ],
        ),
    ]
