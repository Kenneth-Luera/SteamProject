# Generated by Django 5.2.4 on 2025-07-30 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SteamApp', '0007_alter_juegobiblioteca_biblioteca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegobiblioteca',
            name='biblioteca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SteamApp.biblioteca'),
        ),
    ]
