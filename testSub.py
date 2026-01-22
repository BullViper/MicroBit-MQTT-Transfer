import time
import paho.mqtt.client as paho
broker="test.mosquitto.org"
#f = open("results.txt", "a")

#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    #f.write(message.payload)

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect

print("subscribing ")
client.subscribe("CSC548/microbit")#subscribe
client.loop_forever() #start loop to process received messages
time.sleep(1)
