# Generated by Django 2.1.2 on 2018-12-14 03:00

import app.tecnico.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecnico', '0003_auto_20181213_2352'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', app.tecnico.models.UserManager()),
            ],
        ),
    ]
