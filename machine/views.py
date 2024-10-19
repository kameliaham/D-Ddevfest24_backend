from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import MachineData, Machine
from datetime import datetime
from django.db.transaction import atomic, non_atomic_requests
from django.views.decorators.http import require_POST
from django.http import HttpResponse



@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.body)
        return HttpResponse("Webhook received!")
    



@csrf_exempt
@require_POST
def machine_data_webhook(request):
    """
    Receives machine data from the subscription service.
    """

    print("Received data:", request.data)

    data = request.data
    machine_id = data.get('machine_id')
    machine_data = data.get('data') 

    print ("here",machine_id,machine_data)

    # Get the machine by ID or create it if not exists
    try:
        machine = Machine.objects.get(machine_id=machine_id)
        print("machine",machine)
    except Machine.DoesNotExist:
        return Response({"error": "Machine not found"}, status=404)

    # Check if there's a previous record for this machine
    last_machine_data = MachineData.objects.filter(machine=machine).order_by('-timestamp').first()

    # If the data is the same as the last entry, only update the timestamp
    if last_machine_data and last_machine_data.data == machine_data:
        last_machine_data.timestamp = datetime.now()
        last_machine_data.save()
        print("Updated timestamp for identical data")
    else:
        # If the data is new, create a new record
        MachineData.objects.create(machine=machine, data=machine_data, timestamp=datetime.now())
        print("Saved new machine data")

    return Response({"status": "success"}, status=200)
