import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import MachineData, Machine

class MachineDataConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()  # Accepter la connexion WebSocket

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        """
        Méthode appelée à chaque message reçu du frontend.
        """
        text_data_json = json.loads(text_data)
        machine_id = text_data_json.get('machine_id')

        # Récupérer les dernières données de la machine
        machine = Machine.objects.get(machine_id=machine_id)
        latest_data = MachineData.objects.filter(machine=machine).order_by('-timestamp').first()

        # Envoyer les données au client
        if latest_data:
            self.send(text_data=json.dumps({
                'machine_id': machine.machine_id,
                'machine_name': machine.name,
                'data': latest_data.data,
                'timestamp': latest_data.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            }))
