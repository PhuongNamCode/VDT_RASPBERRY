from  Adafruit_IO import  MQTTClient
import random
import time
import sys
class Mqtt:
    client = None
    def __init__(self):
        AIO_USERNAME = "PhuongNamvp160601"
        AIO_KEY = "aio_LcDr77HvneWUX410CEXxZFHJkoIV"
        self.client = MQTTClient(AIO_USERNAME , AIO_KEY)
        self.client.connect()
        self.client.loop_background()
        time.sleep(5)
        
    