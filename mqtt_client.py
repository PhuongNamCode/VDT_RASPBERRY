from  Adafruit_IO import  MQTTClient
from dotenv import load_dotenv
import dotenv
import random
import time
import sys
import os
load_dotenv()
class Mqtt:
    client = None
    def __init__(self):
        AIO_USERNAME = os.getenv('NAME')
        AIO_KEY = os.getenv('KEY')
        print("hi", AIO_USERNAME, AIO_KEY)
        self.client = MQTTClient(AIO_USERNAME , AIO_KEY)
        self.client.connect()
        self.client.loop_background()
        time.sleep(5)
        
    