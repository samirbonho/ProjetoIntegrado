from datetime import datetime
import serial
import time
import struct
import sys
import paho.mqtt.client as mqtt


def com_serial():
    #arduino.flushInput()
    #arduino.flushOutput()
    #time.sleep(1)
    try:
        received_data = arduino.readline()
        time.sleep(1)
        return received_data
    except serial.serialutil.SerialException as e:
            print(e)
            return None
    #print(received_data.decode('Ascii'))


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("samir.bonho@ifsc.edu.br/umidade")
    #client.publish("samir.bonho@ifsc.edu.br/temperatura","28")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client,userdata,result):
    print("data published \n")

if __name__ == "__main__":
    print('Connecting...')
    DEVICE = '/dev/ttyACM0'
    BAUD = 9600
    try:
        arduino = serial.Serial(DEVICE, BAUD)        
    except (OSError,FileNotFoundError) as e:
            print(e)
            sys.exit(1)
    
    client = mqtt.Client()
    client.username_pw_set(username="samir.bonho@ifsc.edu.br",password="ProjetoIFSC822")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.connect("maqiatto.com", 1883, 60)

    while True:

        #client.loop_forever()
        received_frame = com_serial()
        if received_frame is not None:
            data = received_frame.decode('Ascii')
            parse_one = data.split(';')
            auxi = len(parse_one)
            print(auxi)
            for x in range(auxi):
                parse_two = parse_one[x].split('=')
                if parse_two[0] == "temperatura":
                    print(parse_two[1])
                    client.publish("samir.bonho@ifsc.edu.br/temperatura",parse_two[1])                    
                elif parse_two[0] == "umidade":
                    client.publish("samir.bonho@ifsc.edu.br/umidade",parse_two[1])
                elif parse_two[0] == "altura":
                    client.publish("samir.bonho@ifsc.edu.br/altura",parse_two[1])
                elif parse_two[0] == "luminosidade":
                    client.publish("samir.bonho@ifsc.edu.br/luminosidade",parse_two[1])
        else:
            sys.exit(1)
