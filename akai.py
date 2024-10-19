#!/usr/bin/env python3

# inspiration from https://stackoverflow.com/questions/15768066/reading-piano-notes-on-python
# https://www.euclideanspace.com/art/music/midi/codes/index.htm

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


#(b'ALSA', b'Midi Through Port-0', 0, 1, 0)
#(b'ALSA', b'Midi Through Port-0', 1, 0, 0)
#(b'ALSA', b'MPK mini 3 MIDI 1', 0, 1, 0) #output
#(b'ALSA', b'MPK mini 3 MIDI 1', 1, 0, 0) #input
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

def locateMPK():
    for n in range(pygame.midi.get_count()):
        if pygame.midi.get_device_info(n)[1].decode() == 'MPK mini 3 MIDI 1' and pygame.midi.get_device_info(n)[2] == 1:
            print("Found " + pygame.midi.get_device_info(n)[1].decode() + " at id: " + str(n))
            return n

def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            data = event[0]
            command = data[0]
            note_number = data[1]
            velocity = data[2]
            channel = data[3]
            timestamp = event[1]
 
            if velocity == 0:
                continue

            if(note_number == 36):
                print("Pad 1")
                url="http://homeassistant.local:8123/api/webhook/pad1"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)
                continue

            if(note_number == 37):
                print("Pad 2")
                url="http://homeassistant.local:8123/api/webhook/pad2"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)
                continue

            if(note_number == 38):
                print("Pad 3")
                url="http://homeassistant.local:8123/api/webhook/pad3"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)
                continue

            if(note_number == 39):
                print("Pad 4")
                url="http://homeassistant.local:8123/api/webhook/pad4"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)
                continue

            if(note_number == 40):
                print("Pad 5")
                url="http://homeassistant.local:8123/api/webhook/pad5"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)
                continue

            if(note_number == 41):
                print("Pad 6")
                url="http://homeassistant.local:8123/api/webhook/pad6"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)
                continue

            if(note_number == 42):
                print("Pad 7")
                url="http://homeassistant.local:8123/api/webhook/pad7"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)
                continue

            if(note_number == 43):
                print("Pad 8")
                url="http://homeassistant.local:8123/api/webhook/pad8"
                req = request.Request(url, data=reqdata)
                resp = request.urlopen(req)
                continue

            #70-77 Pot 
            #48-72 Keys

            print(note_number)
            print(data)



if __name__ == '__main__':
    pygame.midi.init()
    my_input = pygame.midi.Input(locateMPK())
    readInput(my_input)
