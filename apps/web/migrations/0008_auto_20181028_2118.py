# Generated by Django 2.0.6 on 2018-10-29 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_contacto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aprender',
            options={'verbose_name': 'Aprender', 'verbose_name_plural': 'Aprender'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-fecha_creacion'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'ordering': ['-fecha_creacion'], 'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AlterModelOptions(
            name='suscripcion',
            options={'ordering': ['-fecha_creacion'], 'verbose_name': 'Suscrito', 'verbose_name_plural': 'Suscritos'},
        ),
        migrations.AlterModelOptions(
            name='web',
            options={'verbose_name': 'Webs'},
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de suscripción'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='suscripcion',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de suscripción'),
        ),
    ]
