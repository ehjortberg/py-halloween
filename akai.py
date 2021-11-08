#!/usr/bin/env python3

# inspiration from https://stackoverflow.com/questions/15768066/reading-piano-notes-on-python


import pygame.midi
from urllib import request, parse
import json


reqdata = { 'input': 'akai'}
reqdata = json.dumps(reqdata)
reqdata = str(reqdata)
reqdata = reqdata.encode('utf-8')




def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            data = event[0]
            timestamp = event[1]
            note_number = data[1]
            velocity = data[2]

            if(note_number == 36):
                print("Pad 1")
                url="http://homeassistant.local:8123/api/webhook/pad1"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)

            if(note_number == 37):
                print("Pad 2")
                url="http://homeassistant.local:8123/api/webhook/pad2"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)

            if(note_number == 38):
                print("Pad 3")
                url="http://homeassistant.local:8123/api/webhook/pad3"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)

            if(note_number == 39):
                print("Pad 4")
                url="http://homeassistant.local:8123/api/webhook/pad4"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)

            if(note_number == 40):
                print("Pad 5")
                url="http://homeassistant.local:8123/api/webhook/pad5"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)

            if(note_number == 41):
                print("Pad 6")
                url="http://homeassistant.local:8123/api/webhook/pad6"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)

            if(note_number == 42):
                print("Pad 7")
                url="http://homeassistant.local:8123/api/webhook/pad7"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)

            if(note_number == 43):
                print("Pad 8")
                url="http://homeassistant.local:8123/api/webhook/pad8"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)





# MIDI data from drumpads
# list of midi data, timestamp
# 1 [[[137, 36, 0, 0], 579387]]
# 2 [[[137, 37, 0, 0], 611499]]
# 3 [[[137, 38, 0, 0], 626155]]
# 4 [[[137, 39, 0, 0], 642553]]
# 5 [[[137, 40, 0, 0], 655978]]
# 6 [[[137, 41, 0, 0], 664156]]
# 7 [[[137, 42, 0, 0], 677945]]
# 8 [[[137, 43, 0, 0], 691237]]


# MIDI Devices
# 0 (b'ALSA', b'Midi Through Port-0', 0, 1, 0)
# 1 (b'ALSA', b'Midi Through Port-0', 1, 0, 0)
# 2 (b'ALSA', b'UMC204HD 192k MIDI 1', 0, 1, 0)
# 3 (b'ALSA', b'UMC204HD 192k MIDI 1', 1, 0, 0)
# 4 (b'ALSA', b'MPK mini 3 MIDI 1', 0, 1, 0)
# 5 (b'ALSA', b'MPK mini 3 MIDI 1', 1, 0, 0)



if __name__ == '__main__':

    pygame.midi.init()
    print_devices()

    my_input = pygame.midi.Input(3)
    readInput(my_input)
