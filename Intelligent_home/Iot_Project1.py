# -*- coding: UTF-8 -*-
# !/usr/bin/env python
# 导入模块
from wxpy import *
from datetime import datetime
from azure.storage.blob import BlockBlobService  # upload Picamera pictures to Azure container
from azure.storage.blob import ContentSettings
import picamera
import RPi.GPIO as GPIO
import time
import requests

bot = Bot(cache_path=True)
camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
# The input pin of the sensor will be declared. Additional to that the pull up resistor will be activated
GPIO_PIN1 = 24
GPIO.setup(GPIO_PIN1, GPIO.IN)
subscription_key = "b63b211724b5482cb8abb2c5dffcfe29"
vision_analyze_url = "https://eastasia.api.cognitive.microsoft.com/vision/v1.0/analyze"
print
"start"
# This output function will be started at signal detection
#####buzz###########################################################
GPIO_PIN2 = 23
GPIO.setup(GPIO_PIN2, GPIO.OUT)


################################################################
def outFunction(null):
    print("Signal detected")
    filename = "pircam-" + datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
    camera.capture(filename)
    block_blob_service = BlockBlobService(account_name='project1datalake',
                                          account_key='lcvI6Cq9gI6pNckOc+7kBbXYoUhAL+9j/qMEHkCp9wGZNT8IxJxJwskBrA2mlXq/Um2qIG2DPh5A1fPXrNZWqQ==')
    # block_blob_service.create_blob_from_path('project1container',filename,filename,content_settings=ContentSettings(content_type='image/jpeg'))
    print("uploaded")
    image_path = filename

    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream"}
    params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(vision_analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    analysis = response.json()
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    print(image_caption)

    # The output pin, which is connected with the buzzer, will be declared here.

    # The software-PWM module will be initialized - a frequency of 500Hz will be taken as default.
    Frequenz = 500  # In Hertz
    pwm = GPIO.PWM(GPIO_PIN2, Frequenz)
    pwm.start(50)
    if 'dog' in image_caption:
        print
        "----------------------------------------"
        print
        "Current frequency: %d" % Frequenz
        Frequenz = 200
        pwm.ChangeFrequency(Frequenz)
        time.sleep(10)
        bot.self.send_image(filename)


# At the moment of detection a signal (falling signal edge) the output function will be activated.

GPIO.add_event_detect(GPIO_PIN1, GPIO.FALLING, callback=outFunction, bouncetime=100)

# main program loop
try:
    while True:
        time.sleep(1)

    # Scavenging work after the end of the program
except KeyboardInterrupt:
    GPIO.cleanup()

