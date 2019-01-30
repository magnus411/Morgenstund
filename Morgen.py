# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:27:22 2019

@author: magnu
"""
from pygame import mixer 
import numpy as np
import sounddevice as sd
import pytuya
import time



mixer.init()
mixer.music.load('E:\Github\Git\Prosjekt\Morgenstund\sang.mp3')
duration = 30 #in seconds
b = 0

def lyd():
    print("God morgen")
    mixer.music.play()
    time.sleep(30)
    mixer.music.stop()
    return
    
def listen(indata):
   volume_norm = np.linalg.norm(indata) * 10
   global b
   
   
   if volume_norm > 40 and volume_norm < 60:
       b += 1
       print("HH")
        
   else:
        pass
   if b >= 2:
        lys()
        lyd()
        b = 0
   
    
    
    
    
def lys():
    d = pytuya.OutletDevice('012004765ccf7f605f5d', '10.0.0.124', 'c5a16c13e0559167')
    data = d.status()  # NOTE this does NOT require a valid key
    print('Dictionary %r' % data)
    print('state (bool, true is ON) %r' % data['dps']['1'])  # Show status of first controlled switch on device

    # Toggle switch state
    switch_state = data['dps']['1']
    data = d.set_status(not switch_state)  # This requires a valid key
    if data:
    
        print('set_status() result %r' % data)

    # on a switch that has 4 controllable ports, turn the fourth OFF (1 is the first)

    if data:
    
        print('set_status() result %r' % data)
        print('set_status() extrat %r' % data[20:-8])



        
stream = sd.InputStream(callback=listen)
with stream:
   sd.sleep(duration * 1000)
   
