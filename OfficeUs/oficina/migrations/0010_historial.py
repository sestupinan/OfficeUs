# Generated by Django 2.1.5 on 2020-05-10 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0009_merge_20200510_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.FloatField(blank=True, default=None, null=True)),
                ('tipo', models.CharField(max_length=20)),
                ('fecha_hora', models.CharField(max_length=200)),
                ('arrendatario', models.CharField(max_length=300)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.Oficina')),
            ],
        ),
    ]