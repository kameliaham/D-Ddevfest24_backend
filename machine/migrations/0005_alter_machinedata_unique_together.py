# Generated by Django 5.1.2 on 2024-10-19 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0004_remove_machine_timestamp_agv_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='machinedata',
            unique_together={('machine', 'timestamp')},
        ),
    ]
