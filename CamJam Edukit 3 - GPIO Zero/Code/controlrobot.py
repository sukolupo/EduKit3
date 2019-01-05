# CamJam EduKit 3 - Robotics
#

import time  # Import the Time library
import sys
import termios, tty, os
from gpiozero import CamJamKitRobot, DistanceSensor  # Import the GPIO Zero Libraries

robot = CamJamKitRobot()

# Distance Variables
hownear = 15.0
reversetime = 0.5
turntime = 0.75
sleeptime = 0.1

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.75
rightmotorspeed = 0.75

# incase have put your motors on backwards uncomment these  (like i did)
motorforward = (leftmotorspeed, -rightmotorspeed)
motorbackward = (-leftmotorspeed, rightmotorspeed)
#motorforward = (leftmotorspeed, rightmotorspeed)
#motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (-leftmotorspeed, 0)
motorright = (0, rightmotorspeed)


# Turn right
def turnright():
    print("Right")
    robot.value = motorright
    time.sleep(turntime)
    robot.stop()

def turnleft():
    print("left")
    robot.value = motorleft
    time.sleep(turntime)
    robot.stop()

# Move back a little, then turn right
def backwards():
    # Back off a little
    print("Backwards")
    robot.value = motorbackward
    time.sleep(reversetime)
    robot.stop()

def forwards():
    # Back off a little
    print("Forwards")
    robot.value = motorforward
    time.sleep(reversetime)
    robot.stop()

def uturn():
    print("uturn")
    for x in range(4):
        turnleft()


# create to author recantha
# getch function taken from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
# -----

def main():
    # Your code to control the robot goes below this line
    try:
        # repeat the next indented block forever
        while True:
            key = getch()
            if key == "q": #quit
                break
            if key == "u": 
                uturn()
            elif key == "s": #Down arrow
                backwards()
            elif key == "w": #Up arrow
                forwards()
            elif key == "a": #Left arrow
                turnleft()
            elif key == "d": #Right arrow
                turnright()

            #time.sleep(sleeptime)

               # robot.stop()
              
    # If you press CTRL+C, cleanup and stop
    except KeyboardInterrupt:
        robot.stop()

if (__name__ == '__main__'): 
    main()
