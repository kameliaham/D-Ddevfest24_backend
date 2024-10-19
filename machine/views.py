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
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render


def machine_dashboard(request):
    return render(request, 'machine_dashboard.html')


@csrf_exempt
@require_POST
def machine_data_webhook(request):
    """
    Webhook endpoint to receive real-time machine data from the sensor API.
    """
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    machine_id = data.get('machine_id')
    sensor_data = data.copy()

    try:
        sensor_data['timestamp'] = datetime.fromisoformat(sensor_data['timestamp'].replace("Z", "+00:00"))
        machine_instance = Machine.objects.get(machine_id=machine_id)
        latest_instance = MachineData.objects.filter(machine=machine_instance).order_by('-timestamp').first()

        incoming_data = {k: v for k, v in sensor_data.items() if k not in ['timestamp', 'machine_id']}

        if latest_instance and latest_instance.data == incoming_data:
            latest_instance.timestamp = sensor_data['timestamp']
            latest_instance.save()
        else:
            new_instance = MachineData(
                machine=machine_instance,
                data=incoming_data,
                timestamp=sensor_data['timestamp']
            )
            new_instance.save()

        # Envoyer les nouvelles données à tous les clients WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'machine_data_updates',
            {
                'type': 'machine_data_update',  # Appel de la fonction machine_data_update dans le Consumer
                'data': {
                    'machine_id': machine_id,
                    'data': incoming_data,
                    'timestamp': sensor_data['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                }
            }
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"status": "success"}, status=200)
