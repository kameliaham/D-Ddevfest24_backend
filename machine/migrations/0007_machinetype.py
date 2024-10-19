# Generated by Django 5.1.2 on 2024-10-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0006_remove_cncmachine_machine_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(choices=[('WELDING_ROBOT', 'Welding Robot'), ('STAMPING_PRESS', 'Stamping Press'), ('PAINTING_ROBOT', 'Painting Robot'), ('LEAK_TEST_MACHINE', 'Leak Test Machine'), ('CNC_MILLING', 'CNC Milling'), ('AGV', 'AGV')], max_length=100, unique=True)),
            ],
        ),
    ]