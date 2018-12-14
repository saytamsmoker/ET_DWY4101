# Generated by Django 2.1.2 on 2018-12-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('tecnico', '0004_auto_20181214_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignar',
            name='fk_cli',
        ),
        migrations.AddField(
            model_name='asignar',
            name='fk_cli',
            field=models.ManyToManyField(help_text='Cliente que pidio orden', null=True, to='cliente.Cliente', verbose_name='Cliente Asignado'),
        ),
        migrations.RemoveField(
            model_name='asignar',
            name='fk_tec',
        ),
        migrations.AddField(
            model_name='asignar',
            name='fk_tec',
            field=models.ManyToManyField(help_text='Tecnico que se le asignara Cliente', null=True, to='tecnico.Tecnico', verbose_name='Tecnico a Asignar'),
        ),
    ]