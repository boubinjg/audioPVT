import math
import time
from random import randint
import winsound
import msvcrt
import thread

def input_thread(list):
    while msvcrt.kbhit():
        msvcrt.getch()
    while True:
      if msvcrt.kbhit():
        list.append(None)
        break;
    while msvcrt.kbhit():
        msvcrt.getch()

timeout = time.time() + 3*60;
soundMaxLength = 30;
lowsound = 10;
#3 minute outer loop
while time.time() < timeout:
  silence = randint(5,10)
  print(silence)
  time.sleep(silence)
  maxTime = time.time() + soundMaxLength
  maxLowSound = time.time() + lowsound;
  list = []
  thread.start_new_thread(input_thread, (list,))

  while time.time() < maxTime and not list:
    if time.time() <  maxLowSound:
      print("low sound")
      winsound.Beep(2500, 475) #2500hz sound, 475ms
      waitlength = 0.048
      time.sleep(waitlength)
    else:
      print("high sound")
      winsound.Beep(5000, 475) #2500hz sound, 475ms
      waitlength = 0.048
      time.sleep(waitlength) 
