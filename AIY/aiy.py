#!/usr/bin/env python3
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import aiy.i18n
import RPi.GPIO as GPIO
from time import sleep
import serial
import random
import pygame
ser = serial.Serial('/dev/ttyACM0',115200)
sleep(5) # wait for Arduino ready
#ser.write(b"Waiting Arduino \n")
#ser.flush()
#sleep(1)
pygame.init()

#def main():
print("setup...")
recognizer = aiy.cloudspeech.get_recognizer()
recognizer.expect_phrase('turn on the light')
recognizer.expect_phrase('turn off the light')
recognizer.expect_phrase('turn on')
recognizer.expect_phrase('turn off')
recognizer.expect_phrase('music')
recognizer.expect_phrase('stop')
recognizer.expect_phrase('hello')
button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()
aiy.audio.get_recorder().start()

####################

import logging
import sys

import aiy.assistant.auth_helpers
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def process_event(event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)

#################
while True:
    print('Press the button and speak')
    button.wait_for_press()
    print('Listening...')
    text = recognizer.recognize()
    if text is None:
        print('Sorry, I did not hear you.')
        
    else:
        print('You said "', text, '"')
        if 'turn on the light' in text:
            led.set_state(aiy.voicehat.LED.ON)            
            ser.write(b"1\n")
            ser.flush()
            print('ok,turn on')     
            
        elif 'turn off the light' in text:
            led.set_state(aiy.voicehat.LED.ON)            
            ser.write(b"2\n")
            ser.flush()
            print('ok,turn off')     

        elif 'turn on' in text:
            led.set_state(aiy.voicehat.LED.ON)            
            ser.write(b"3\n")
            ser.flush()
            print('ok,fan turn on')
        elif 'turn off' in text:
            led.set_state(aiy.voicehat.LED.ON)            
            ser.write(b"4\n")
            ser.flush()
            print('ok,fan turn off')  
        elif 'music' in text:
            a=random.randint(0,3)
            print(a)
            pygame.mixer.init()
            pygame.mixer.music.load('/home/pi/Desktop/{}.mp3'.format(a))
            pygame.mixer.music.play()            
            pygame.mixer.music.fadeout(5000)

         
        elif 'hello' in text: 
            credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
            with Assistant(credentials) as assistant:
                for event in assistant.start():
                    process_event(event)
            #flag2=flag2+1
            #print(flag)
            #if flag2==12:
                #break
                
            

#if __name__ == '__main__':
    #main()

#######################################
#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""


#def main():
    #credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    #with Assistant(credentials) as assistant:
        #for event in assistant.start():
            #process_event(event)


#if __name__ == '__main__':
    #main()



