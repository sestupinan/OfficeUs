# Generated by Django 2.1.5 on 2020-05-10 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0010_historial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='tipo_cliente',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
