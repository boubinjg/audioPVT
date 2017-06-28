import time
from random import randint
import winsound
import msvcrt
import thread

#This is a list of the reaction times (ms) for each key press
reactionTimes = [];
#duration of the entire test in seconds
testDuration = 45;
timeout = time.time() + testDuration;
#maximum length the beep (high or low pitch) will sound before timing out
soundMaxLength = 30;
#duration of the lower pitched sound before the higher pitched sound begins
lowsound = 10;
#beginning time of a given sound loop
beginTime = time.time()

'''
This function is executed by a thread which waits for a key press.
It will wait for a press, then signal the main function to stop execution
of the sound loop by appending a null variable to shared list.
'''
def input_thread(list):
    #flush buffer incase of leftover keypresses
    while msvcrt.kbhit():
        msvcrt.getch()

    threadBegin = time.time()
    #wait for key press
    while True:
      if msvcrt.kbhit():
        #signal main thread
        list.append(None)
        #append the reaction time to the list
        reactionTimes.append((time.time() - beginTime)*1000)
        #exit loop
        break;
      elif time.time() > threadBegin+soundMaxLength:
        list.append(None)
        reactionTimes.append(30000)
        break;
    #flush buffer incase of multiple key presses
    while msvcrt.kbhit():
        msvcrt.getch()

#loop until timeout
while time.time() < timeout:
  #get a random integer between 5 and 10 representing the length of silence (s)
  silence = randint(5,10)
  #sleep for a number of seconds equal to 'silence'
  time.sleep(silence)
  #store the timeout for the total sound
  maxTime = time.time() + soundMaxLength
  #store the timeout for the low sound
  maxLowSound = time.time() + lowsound;

  #create signal variable to determine when sound loop should stop on key press
  signal = []
  #dispatch keypress thread
  thread.start_new_thread(input_thread, (signal,))

  #store time at beginning of sound loop for reaction time calculation
  beginTime = time.time()

  #loop until timeout or keypress
  while time.time() < maxTime and not signal:

    #if still emiting low sound
    if time.time() <  maxLowSound:
      #create low sound
      winsound.Beep(2000, 475) #2500hz sound, 475ms
      #gap between low sound
      waitlength = 0.048
      #sleep for 'waitlength' seconds
      time.sleep(waitlength)

    #high sound
    else:
      #create high sound
      winsound.Beep(5000, 475) #5000hz sound, 475ms
      #gap between low sound
      waitlength = 0.048
      #sleep for 'waitlength' seconds
      time.sleep(waitlength)

#print reaction times
output = open("audioPVToutput.txt","w+")
for s in reactionTimes:
  output.write(str(s))
  output.write("\n")
output.close()
sleep(5)

