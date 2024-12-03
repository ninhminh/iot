import paho.mqtt.client as mqtt
import json

# Thông tin về broker MQTT
MQTT_BROKER = "localhost"  # Thay bằng broker của bạn
MQTT_PORT = 1883
MQTT_TOPIC = "iot/system"

# Callback khi kết nối thành công
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)

# Callback khi nhận được thông điệp
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    print(f"Received message: {payload}")

    # Xử lý dữ liệu, ví dụ điều khiển bơm
    if payload.get("pumpState") is not None:
        control_pump(payload["pumpState"])

# Hàm điều khiển bơm
def control_pump(state):
    print(f"Pump state: {'ON' if state else 'OFF'}")

# Cấu hình MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print("Kết nối thành công đến broker MQTT!")
except Exception as e:
    print(f"Lỗi kết nối: {e}")

# Kết nối với MQTT Broker
def start_mqtt():
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

