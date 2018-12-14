# Generated by Django 2.1.2 on 2018-12-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnico', '0005_auto_20181214_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar',
            name='fk_cli',
            field=models.ManyToManyField(help_text='Cliente que pidio orden', to='cliente.Cliente', verbose_name='Cliente Asignado'),
        ),
        migrations.AlterField(
            model_name='asignar',
            name='fk_tec',
            field=models.ManyToManyField(help_text='Tecnico que se le asignara Cliente', to='tecnico.Tecnico', verbose_name='Tecnico a Asignar'),
        ),
    ]