# Generated by Django 2.1 on 2018-09-12 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rouboapi', '0002_respage01'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Respage01',
            new_name='Respage01Info',
        ),
        migrations.AlterModelTable(
            name='respage01info',
            table='respage01',
        ),
    ]
