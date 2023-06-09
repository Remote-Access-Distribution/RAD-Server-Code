import paho.mqtt.client as mqtt
import json
 
# Handles the actual transmission of the MQTT messages
def send_mqtt_message(distro, socket, state):
    client = mqtt.Client()
    client.connect("localhost", 1883)
    data = {'socket': socket, 'state': state}
    payload = json.dumps(data)
    client.publish("distro/"+distro, payload)
    client.disconnect()
