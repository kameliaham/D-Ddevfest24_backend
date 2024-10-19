# Generated by Django 5.1.2 on 2024-10-19 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0007_machinetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='machine_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='machine.machinetype'),
        ),
    ]
