import paho.mqtt.client as paho
import serial
broker = "test.mosquitto.org"
port = 1883

serialport = serial.Serial("COM5", 115200, timeout=0.5)


client= paho.Client("SerialPublish")

print("connecting to broker ",broker)
client.connect(broker)#connect
time.sleep(2)

while True:
	input = serialport.read()
	client.publish("CSC548/microbit",input)
	pass

time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop
