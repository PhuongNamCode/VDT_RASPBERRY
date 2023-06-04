from  Adafruit_IO import  MQTTClient
from mqtt_client import *
import random
import time
import sys
class Task1:
    client = None
    def __init__(self):
       self.client = Mqtt().client
       print("Init task 1")
   
    def Task1_Run(self):
        # print("Task 1 is activated!!!!")
        value = random.randint(0, 100)
        self.client.publish("your_feed", value)
        print("value:", value)
        # time.sleep(5)