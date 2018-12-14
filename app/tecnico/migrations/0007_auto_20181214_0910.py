# Generated by Django 2.1.2 on 2018-12-14 12:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnico', '0006_auto_20181214_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar',
            name='fk_tec',
            field=models.ManyToManyField(help_text='Tecnico que se le asignara Cliente', to=settings.AUTH_USER_MODEL, verbose_name='Tecnico a Asignar'),
        ),
    ]