# Generated by Django 3.2.8 on 2021-11-06 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvrp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='courier',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='depot',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
    ]
