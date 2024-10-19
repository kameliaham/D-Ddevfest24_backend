from django.db import models
from django.utils import timezone


class Machine(models.Model): 
    machine_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()  

    def __str__(self):
        return f"{self.name} ({self.machine_id})"


class WeldingRobot(Machine):
    weld_temperature = models.FloatField()  # °C
    weld_current = models.FloatField()  # A
    weld_voltage = models.FloatField()  # V
    weld_time = models.IntegerField()  # ms
    pressure_applied = models.FloatField()  # N
    arm_position = models.JSONField()  # Spatial coordinates (x, y, z)
    wire_feed_rate = models.FloatField()  # mm/min
    gas_flow_rate = models.FloatField()  # l/min
    weld_strength_estimate = models.FloatField()  # N
    vibration_level = models.FloatField()  # mm/s
    power_consumption = models.FloatField()  # kWh


class StampingPress(Machine):
    force_applied = models.FloatField()  # tons
    cycle_time = models.FloatField()  # seconds
    temperature = models.FloatField()  # °C
    vibration_level = models.FloatField()  # mm/s
    cycle_count = models.IntegerField()  # count
    oil_pressure = models.FloatField()  # bar
    die_alignment = models.CharField(max_length=50)  # e.g., "aligned"
    sheet_thickness = models.FloatField()  # mm
    power_consumption = models.FloatField()  # kWh
    noise_level = models.FloatField()  # dB
    lubrication_flow_rate = models.FloatField()  # ml/min


class PaintingRobot(Machine):
    spray_pressure = models.FloatField()  # bar
    paint_thickness = models.FloatField()  # µm
    arm_position = models.JSONField()  # Spatial coordinates (x, y, z)
    temperature = models.FloatField()  # °C
    humidity = models.FloatField()  # %RH
    paint_flow_rate = models.FloatField()  # ml/min
    paint_volume_used = models.FloatField()  # liters
    atomizer_speed = models.IntegerField()  # RPM
    overspray_capture_efficiency = models.FloatField()  # %
    booth_airflow_velocity = models.FloatField()  # m/s
    solvent_concentration = models.FloatField()  # %


class AGV(Machine):
    location = models.JSONField()  # Spatial coordinates (x, y, z)
    battery_level = models.FloatField()  # %
    load_weight = models.FloatField()  # kg
    speed = models.FloatField()  # m/s
    distance_traveled = models.FloatField()  # meters
    obstacle_detection = models.BooleanField()  # True/False
    navigation_status = models.CharField(max_length=50)  # e.g., "en_route", "waiting", "rerouting"
    vibration_level = models.FloatField()  # mm/s
    temperature = models.FloatField()  # °C
    wheel_rotation_speed = models.FloatField()  # RPM


class CNCMachine(Machine):
    spindle_speed = models.IntegerField()  # RPM
    tool_wear_level = models.FloatField()  # %
    cut_depth = models.FloatField()  # mm
    feed_rate = models.FloatField()  # mm/min
    vibration_level = models.FloatField()  # mm/s
    coolant_flow_rate = models.FloatField()  # ml/min
    material_hardness = models.FloatField()  # HB
    power_consumption = models.FloatField()  # kWh
    temperature = models.FloatField()  # °C
    chip_load = models.FloatField()  # mm

class LeakTestMachine(Machine):
    test_pressure = models.FloatField()  # bar
    pressure_drop = models.FloatField()  # bar
    leak_rate = models.FloatField()  # ml/min
    test_duration = models.IntegerField()  # seconds
    temperature = models.FloatField()  # °C
    status = models.CharField(max_length=50)  # e.g., "pass", "fail"
    fluid_type = models.CharField(max_length=50)  # e.g., "air", "water"
    seal_condition = models.CharField(max_length=50)  # e.g., "good", "warning", "fail"
    test_cycle_count = models.IntegerField()  # number of test cycles


class MachineData(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    data = models.JSONField()  
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Data for {self.machine.name} at {self.timestamp}"
