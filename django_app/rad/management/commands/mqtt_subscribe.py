from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from rad.models import DistroCurrentData
import paho.mqtt.client as mqtt
import json

class Command(BaseCommand):
    help = 'Subscribes to an MQTT topic and saves the data to the database'

    def add_arguments(self, parser):
        parser.add_argument('topic', type=str, help='The MQTT topic to subscribe to')
        parser.add_argument('--broker', type=str, default='localhost', help='The MQTT broker host (default: localhost)')
        parser.add_argument('--port', type=int, default=1883, help='The MQTT broker port (default: 1883)')

    def handle(self, *args, **options):
        def on_connect(client, userdata, flags, rc):
            print('Connected with result code', rc)
            client.subscribe(options['topic'])

        def on_message(client, userdata, msg):
            payload=msg.payload.decode('utf-8')
            data = json.loads(payload)
            mqtt_data = None
            if "current" in msg.topic:
                mqtt_data = DistroCurrentData.objects.create(
                    distroID=msg.topic[7 : len(msg.topic)-8],
                    socketNum=data['socket'],
                    currentValue=data['value'],
                    timestamp=timezone.now()
                )
                
                print('Saved MQTT data:', mqtt_data)

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(options['broker'], options['port'], 60)
        client.loop_forever()
