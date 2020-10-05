import random
import ctypes
from datetime import datetime
import serial
import time
import struct
import paho.mqtt.client as paho



def com_serial():
    #arduino.flushInput()
    #arduino.flushOutput()
    #time.sleep(1)
    received_data = arduino.readline()
    #print(received_data.decode('Ascii'))
    time.sleep(1)
    return received_data


if __name__ == "__main__":
    print('Connecting...')
    DEVICE = '/dev/ttyACM0'
    BAUD = 9600
    arduino = serial.Serial(DEVICE, BAUD)

    while True:

        received_frame = com_serial()
        data = received_frame.decode('Ascii')
        print(data)
        parse_one = data.split(';')
        auxi = len(parse_one)
        print(auxi)
        for x in range(auxi):
            parse_two = parse_one[x].split('=');
            if parse_two[0] == "temperatura":
                print(parse_two[1])
            elif parse_two[0] == "umidade":
                print(parse_two[1])
            elif parse_two[0] == "altura":
                print("te falei")
        #Print the contents of the serial data
        
