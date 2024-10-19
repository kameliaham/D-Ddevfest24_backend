from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import *
from datetime import datetime
from django.db.transaction import atomic, non_atomic_requests
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json



@csrf_exempt
@require_POST
def machine_data_webhook(request):
    """
    Webhook endpoint to receive real-time machine data from the sensor API.
    """
    try:
        data = json.loads(request.body)  # Parse incoming JSON data
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    machine_id = data.get('machine_id')
    sensor_data = data.copy()  # Make a copy to preserve original data

    try:
        sensor_data['timestamp'] = datetime.fromisoformat(sensor_data['timestamp'].replace("Z", "+00:00"))
        # Retrieve the latest instance of MachineData for this machine_id
        machine_instance = Machine.objects.get(machine_id=machine_id)
        latest_instance = MachineData.objects.filter(machine=machine_instance).order_by('-timestamp').first()

        if latest_instance:
            # Check if incoming data (excluding timestamp and machine_id) is the same as the latest instance's data
            incoming_data = {k: v for k, v in sensor_data.items() if k not in ['timestamp', 'machine_id']}
            if latest_instance.data == incoming_data:
                # If the data is the same, update the timestamp
                latest_instance.timestamp = sensor_data['timestamp']
                latest_instance.save()
            else:
                # Create a new instance with the updated data
                machine_instance = MachineData(
                    machine=latest_instance.machine,
                    data=incoming_data,  # Exclude timestamp and machine_id
                    timestamp=sensor_data['timestamp']
                )
                machine_instance.save()
        else:
            # Create a new instance if no previous instance exists
            incoming_data = {k: v for k, v in sensor_data.items() if k not in ['timestamp', 'machine_id']}
            machine_instance = MachineData(
                machine=machine_instance,
                data=incoming_data, 
                timestamp=sensor_data['timestamp']
            )
            machine_instance.save()

    except Exception as e:
        print("here error", e)
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"status": "success"}, status=200)



