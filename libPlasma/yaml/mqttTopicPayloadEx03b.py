
import paho.mqtt.client as mqtt
import json

# Define MQTT broker details
BROKER = "mqtt.eclipse.org"
PORT = 1883

# Define topics
TOPIC_SENSE     = "sense/schoolroom1/temperature"
TOPIC_ALERT     = "alert/forestgrid/fire"
TOPIC_INTERACT  = "interact/classroom1/token"
TOPIC_VISUALIZE = "visualize/classroom1/screens"

# Define message payloads
sense_payload = {"sensor_id": "sensor_123", "timestamp": "2025-06-07T20:30:00Z",
                 "location": "classroom_1", "data_type": "float", "value": 22.5 }

alert_payload = {"severity": "high",        "timestamp": "2025-06-07T20:35:00Z",
                 "affected_area": "sector_7", "instructions": "evacuate immediately", "ack_required": True }

interact_payload = {"user_id": "student_42", "timestamp": "2025-06-07T20:40:00Z",
                    "device_id": "nfc_reader_1", "gesture": "token_swipe", "context": "lesson_navigation" }

visualize_payload = {"source": "sensor_cluster_alpha", "mode": "timeline", "interactivity": True,
                    "annotations": ["thresholds", "alerts"], "layout": "horizontal_strip",
                    "locations": ["classroom_1", "classroom_2"] }

# Define the MQTT client
client = mqtt.Client()

# Define the on_connect callback
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    for t in [TOPIC_SENSE, TOPIC_ALERT, TOPIC_INTERACT, TOPIC_VISUALIZE]:
      client.subscribe(t)

# Define the on_message callback
def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

# Set callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(BROKER, PORT, 60)

# Publish messages
client.publish(TOPIC_SENSE, json.dumps(sense_payload))
client.publish(TOPIC_ALERT, json.dumps(alert_payload))
client.publish(TOPIC_INTERACT, json.dumps(interact_payload))
client.publish(TOPIC_VISUALIZE, json.dumps(visualize_payload))

# Start the loop
client.loop_start()

# Keep the script running to listen for messages
try:
  while True: pass

except KeyboardInterrupt:
  client.loop_stop()
  client.disconnect()

### end ###
