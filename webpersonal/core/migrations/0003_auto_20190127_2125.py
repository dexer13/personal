# Generated by Django 2.1.4 on 2019-01-28 02:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190127_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacionpersonal',
            name='descripcion',
            field=ckeditor.fields.RichTextField(default='No hay descripción'),
        ),
        migrations.AlterField(
            model_name='informacionpersonal',
            name='hab_blandas',
            field=ckeditor.fields.RichTextField(default='No hay habilidades blandas'),
        ),
        migrations.AlterField(
            model_name='informacionpersonal',
            name='hab_tecnicas',
            field=ckeditor.fields.RichTextField(default='No hay habilidades técnicas'),
        ),
    ]