# Generated by Django 2.1.2 on 2018-12-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnico', '0007_auto_20181214_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar',
            name='id_as',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]