# Generated by Django 3.0.5 on 2020-12-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto_ya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'fecilitaciones']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
