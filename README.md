# MicroBit-MQTT-Transfer
This project contains code that uses an MQTT (Message Queue Telemetry Transport) framework to send messages from microbits


Links: 

https://microbit.org/

https://www.raspberrypi.com/

https://mqtt.org/

https://pypi.org/project/paho-mqtt/


This code functions as a template for creating a sensor network with microbits. This can theoretically be modified to allow any other radio-based messages to be transmitted and recorded.
The network functions as follows:

```mermaid
flowchart LR

    subgraph Edge["Edge Devices"]
        TX["Radio Timer Sender<br/>micro:bit<br/>MicroPython"]
        RX["Radio Receiver<br/>micro:bit<br/>MicroPython / MakeCode"]
    end

    subgraph Gateway["Gateway"]
        Serial["USB Serial Bridge<br/>pySerial<br/>PC"]
    end

    subgraph Messaging["Messaging Layer"]
        Broker["MQTT Broker<br/>TCP<br/>mosquitto (test.mosquitto.org)"]
    end

    subgraph App["Application"]
        Pub["Serial → MQTT Publisher<br/>Python · paho"]
        Sub["MQTT Subscriber<br/>Python · paho"]
    end

    subgraph Storage["Storage"]
        File["Text / Log File"]
    end

    TX -->|micro:bit Radio| RX
    RX -->|USB Serial| Serial
    Serial -->|Raw Text| Pub
    Pub -->|MQTT TCP| Broker
    Broker -->|MQTT TCP| Sub
    Sub -->|Append| File

```

