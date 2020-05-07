# Generated by Django 2.1.5 on 2020-05-02 00:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0004_oficina_parqueadero'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficina',
            name='agua',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='aire',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='cafe',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='calefaccion',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='chillout',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='dog',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='eventos',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='fotocopiadora',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='impresora',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='locker',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='moditorunico',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='monitordual',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='proyector',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='scanner',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='transporte',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='vista',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oficina',
            name='wifi',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]