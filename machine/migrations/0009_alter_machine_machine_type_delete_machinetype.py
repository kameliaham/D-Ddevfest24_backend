# Generated by Django 5.1.2 on 2024-10-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0008_machine_machine_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='machine_type',
            field=models.CharField(choices=[('WELDING_ROBOT', 'Welding Robot'), ('STAMPING_PRESS', 'Stamping Press'), ('PAINTING_ROBOT', 'Painting Robot'), ('LEAK_TEST_MACHINE', 'Leak Test Machine'), ('CNC_MILLING', 'CNC Milling'), ('AGV', 'AGV')], max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='MachineType',
        ),
    ]
