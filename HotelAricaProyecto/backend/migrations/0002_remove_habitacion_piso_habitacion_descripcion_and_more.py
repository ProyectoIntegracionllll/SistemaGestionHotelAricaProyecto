# Generated by Django 4.2.4 on 2023-12-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='piso',
        ),
        migrations.AddField(
            model_name='habitacion',
            name='descripcion',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='estado',
            field=models.CharField(choices=[('disponible', 'Disponible'), ('ocupada', 'Ocupada'), ('mantenimiento', 'Mantenimiento')], default='disponible', max_length=15),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='tipo',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Doble', 'Doble'), ('Suite', 'Suite'), ('Deluxe', 'Deluxe')], max_length=15),
        ),
    ]
