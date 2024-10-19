from django.db import models
from django.utils import timezone
from enum import Enum


# Define an enumeration for different types of machines.
class MachineTypes(Enum):
    WELDING_ROBOT = "Welding Robot"
    STAMPING_PRESS = "Stamping Press"
    PAINTING_ROBOT = "Painting Robot"
    LEAK_TEST_MACHINE = "Leak Test Machine"  
    CNC_MILLING = "CNC Milling"
    AGV = "AGV"


# Define the Machine model, representing any type of machine in the system.
class Machine(models.Model): 
    machine_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    machine_type = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in MachineTypes],
        default=MachineTypes.WELDING_ROBOT.value  
    )
    def __str__(self):
        return f"{self.name} ({self.machine_id})"
  

# Define the MachineData model, which stores data related to any machine.
class MachineData(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    data = models.JSONField()  
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (('machine', 'timestamp'),)

    def __str__(self):
        return f"Data for {self.machine.name} at {self.timestamp}"
