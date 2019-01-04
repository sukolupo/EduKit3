# CamJam EduKit 3 - Robotics
#

import time  # Import the Time library
#import sys
#from msvcrt import getch
import pygame, sys
from pygame.locals import *
from gpiozero import CamJamKitRobot, DistanceSensor  # Import the GPIO Zero Libraries

robot = CamJamKitRobot()

# Distance Variables
hownear = 15.0
reversetime = 0.5
turntime = 0.75
sleeptime = 0.1

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 0.5
rightmotorspeed = 0.5

# incase have put your moters on backwards uncomment these  (like i did)
motorforward = (-leftmotorspeed, -rightmotorspeed)
motorbackward = (leftmotorspeed, rightmotorspeed)
#motorforward = (leftmotorspeed, rightmotorspeed)
#motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
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
    turnleft()
    turnleft()

def main():
    pygame.init()
    BLACK = (0,0,0)
    WIDTH = 100
    HEIGHT = 100
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    windowSurface.fill(BLACK)
    # Your code to control the robot goes below this line
    try:
        # repeat the next indented block forever
        while True:
               for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        key = event.key
                        if key == pygame.K_KP_ENTER: #Enter
                            uturn()
                        elif key == pygame.K_DOWN: #Down arrow
                            backwards()
                        elif key == pygame.K_UP: #Up arrow
                            forwards()
                        elif key == pygame.K_LEFT: #Left arrow
                            turnleft()
                        elif key == pygame.K_RIGHT: #Right arrow
                            turnright()

                    time.sleep(sleeptime)

               # robot.stop()
              
    # If you press CTRL+C, cleanup and stop
    except KeyboardInterrupt:
        robot.stop()

if (__name__ == '__main__'): 
    main()
