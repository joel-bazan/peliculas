# Generated by Django 4.1.6 on 2023-03-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mispeliculas', '0005_capitulo_visto'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulo',
            name='descripcion',
            field=models.CharField(default='Nuevo Capítulo', max_length=500),
        ),
    ]
