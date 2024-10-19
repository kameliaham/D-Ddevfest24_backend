from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Machine, WeldingRobot, StampingPress, PaintingRobot, AGV, CNCMachine, LeakTestMachine


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['machine_id', 'name', 'type', 'timestamp']


class WeldingRobotSerializer(MachineSerializer):
    weld_temperature = serializers.FloatField()
    weld_current = serializers.FloatField()
    weld_voltage = serializers.FloatField()
    weld_time = serializers.IntegerField()
    pressure_applied = serializers.FloatField()
    arm_position = serializers.JSONField()
    wire_feed_rate = serializers.FloatField()
    gas_flow_rate = serializers.FloatField()
    weld_strength_estimate = serializers.FloatField()
    vibration_level = serializers.FloatField()
    power_consumption = serializers.FloatField()

    class Meta:
        model = WeldingRobot
        fields = MachineSerializer.Meta.fields + ['weld_temperature', 'weld_current', 'weld_voltage', 'weld_time', 'pressure_applied', 'arm_position', 'wire_feed_rate', 'gas_flow_rate', 'weld_strength_estimate', 'vibration_level', 'power_consumption']

class StampingPressSerializer(MachineSerializer):
    force_applied = serializers.FloatField()
    cycle_time = serializers.FloatField()
    temperature = serializers.FloatField()
    vibration_level = serializers.FloatField()
    cycle_count = serializers.IntegerField()
    oil_pressure = serializers.FloatField()
    die_alignment = serializers.CharField(max_length=50)
    sheet_thickness = serializers.FloatField()
    power_consumption = serializers.FloatField()
    noise_level = serializers.FloatField()
    lubrication_flow_rate = serializers.FloatField()

    class Meta:
        model = StampingPress
        fields = MachineSerializer.Meta.fields + ['force_applied', 'cycle_time', 'temperature', 'vibration_level', 'cycle_count', 'oil_pressure', 'die_alignment', 'sheet_thickness', 'power_consumption', 'noise_level', 'lubrication_flow_rate']


class PaintingRobotSerializer(MachineSerializer):
    spray_pressure = serializers.FloatField()
    paint_thickness = serializers.FloatField()
    arm_position = serializers.JSONField()
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    paint_flow_rate = serializers.FloatField()
    paint_volume_used = serializers.FloatField()
    atomizer_speed = serializers.IntegerField()
    overspray_capture_efficiency = serializers.FloatField()
    booth_airflow_velocity = serializers.FloatField()
    solvent_concentration = serializers.FloatField()

    class Meta:
        model = PaintingRobot
        fields = MachineSerializer.Meta.fields + ['spray_pressure', 'paint_thickness', 'arm_position', 'temperature', 'humidity', 'paint_flow_rate', 'paint_volume_used', 'atomizer_speed', 'overspray_capture_efficiency', 'booth_airflow_velocity', 'solvent_concentration']


class AGVSerializer(MachineSerializer):
    location = serializers.JSONField()
    battery_level = serializers.FloatField()
    load_weight = serializers.FloatField()
    speed = serializers.FloatField()
    distance_traveled = serializers.FloatField()
    obstacle_detection = serializers.BooleanField()
    navigation_status = serializers.CharField(max_length=50)
    vibration_level = serializers.FloatField()
    temperature = serializers.FloatField()
    wheel_rotation_speed = serializers.FloatField()

    class Meta:
        model = AGV
        fields = MachineSerializer.Meta.fields + ['location', 'battery_level', 'load_weight', 'speed', 'distance_traveled', 'obstacle_detection', 'navigation_status', 'vibration_level', 'temperature', 'wheel_rotation_speed']



class CNCMachineSerializer(MachineSerializer):
    spindle_speed = serializers.IntegerField()
    tool_wear_level = serializers.FloatField()
    cut_depth = serializers.FloatField()
    feed_rate = serializers.FloatField()
    vibration_level = serializers.FloatField()
    coolant_flow_rate = serializers.FloatField()
    material_hardness = serializers.FloatField()
    power_consumption = serializers.FloatField()
    temperature = serializers.FloatField()
    chip_load = serializers.FloatField()

    class Meta:
        model = CNCMachine
        fields = MachineSerializer.Meta.fields + ['spindle_speed', 'tool_wear_level', 'cut_depth', 'feed_rate', 'vibration_level', 'coolant_flow_rate', 'material_hardness', 'power_consumption', 'temperature', 'chip_load']


class LeakTestMachineSerializer(MachineSerializer):
    test_pressure = serializers.FloatField()
    pressure_drop = serializers.FloatField()
    leak_rate = serializers.FloatField()
    test_duration = serializers.IntegerField()
    temperature = serializers.FloatField()
    status = serializers.CharField(max_length=50)
    fluid_type = serializers.CharField(max_length=50)
    seal_condition = serializers.CharField(max_length=50)
    test_cycle_count = serializers.IntegerField()

    class Meta:
        model = LeakTestMachine
        fields = MachineSerializer.Meta.fields + ['test_pressure', 'pressure_drop', 'leak_rate', 'test_duration', 'temperature', 'status', 'fluid_type', 'seal_condition', 'test_cycle_count']
