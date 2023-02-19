# Generated by Django 4.1.6 on 2023-02-19 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('director', models.CharField(blank=True, max_length=200)),
                ('descargada', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('temporadas', models.IntegerField(default=1)),
                ('completada', models.BooleanField(default=False)),
                ('descargada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=0)),
                ('temporada', models.IntegerField(default=0)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mispeliculas.serie')),
            ],
        ),
    ]
