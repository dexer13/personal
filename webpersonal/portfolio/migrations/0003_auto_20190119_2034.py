# Generated by Django 2.1.4 on 2019-01-20 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190119_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='urlfield',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='enlace'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha creación'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portafolio', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, verbose_name='titulo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha actualización'),
        ),
    ]