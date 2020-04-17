# Generated by Django 2.2 on 2020-04-17 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField(blank=True, default=None, null=True)),
                ('tipo_contrato', models.CharField(max_length=20)),
                ('ubicacion', models.CharField(max_length=40)),
                ('localidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('barrio', models.CharField(max_length=30)),
                ('foto', models.CharField(max_length=100)),
            ],
        ),
    ]
