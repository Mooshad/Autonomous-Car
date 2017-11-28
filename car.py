from random import *
from scipy import interpolate
import numpy as np
import math


class car:
    # Initialize car.
    # lane is a lane in the world
    # vel is a 2d vector containing current x and y velocity.
    # acc is a 2d vector containing current x and y acceleration.
    def __init__(self, lane, color):
        self.position = lane.scp
        self.lane = lane
        self.lane_index = lane.index
        self.acc = 0
        self.color = color
        self.time = 0
        self.vel = randint(3,5)
        # Records the last position the car was at,
        # is used to capture the heading for displaying
        self.last_position = None

        # Set initial car rotation
        if (lane.index > 2 and lane.index <= 5) or (lane.index > 8 and lane.index <= 11):
            self.rotation = 90.0
        else:
            self.rotation = 0.0
        
    # On tick, update velocity and acceleration
    def on_tick(self, new_acc):

        self.last_position = self.position
        self.vel = self.vel + self.acc

        lane = self.lane
        # Handle case when car hasn't entered the intersection yet
        if before_intersection(self):
            
            if lane.index >= 0 and lane.index <= 2:
                self.position[0] = self.position[0] + self.vel
            elif lane.index > 2 and lane.index <= 5:
                self.position[1] = self.position[1] + self.vel
            elif lane.index > 5 and lane.index <= 8:
                self.position[0] = self.position[0] - self.vel
            elif lane.index > 8 and lane.index <= 11:
                self.position[1] = self.position[1] - self.vel

        # Handle case when car has already made it through the intersection
        # Also handles car rotation for after the intersection
        elif after_intersection(self):
            if lane.index == 11 or lane.index == 7 or lane.index == 3:
                self.position[0] = self.position[0] - self.vel
                self.rotation = 0.0
            elif lane.index == 2 or lane.index == 10 or lane.index == 6:
                self.position[1] = self.position[1] - self.vel
                self.rotation = 90.0
            elif lane.index == 9 or lane.index == 1 or lane.index == 5:
                self.position[0] = self.position[0] + self.vel
                self.rotation = 0.0
            elif lane.index == 0 or lane.index == 4 or lane.index == 8:
                self.position[1] = self.position[1] + self.vel
                self.rotation = 90.0
                
        # Handle traveling direction when in the intersection through
        # interpolation. Also find new car rotation based off direction
        # vector.
        else:
            self.position = intersection_pos(self)
        
        self.acc = new_acc
        self.time = self.time + 1

            
def check_collision(car1, car2):
    pass


# Check if car hasn't entered the intersection yet    
def before_intersection(car):
    lane = car.lane
    l_index = lane.index
    pos = car.position

    # Left lanes
    if l_index == 0:
        return pos[0] < lane.sip[0]
    elif l_index == 1:
        return pos[0] < lane.sip[0]
    elif l_index == 2:
        return pos[0] < lane.sip[0]
    
    # Bottom lanes
    elif l_index == 3:
        return pos[1] < lane.sip[1]
    elif l_index == 4:
        return pos[1] < lane.sip[1]
    elif l_index == 5:
        return pos[1] < lane.sip[1]

    # Right lanes
    elif l_index == 6:
        return pos[0] > lane.sip[0]
    elif l_index == 7:
        return pos[0] > lane.sip[0]
    elif l_index == 8:
        return pos[0] > lane.sip[0]

    # Top lanes
    elif l_index == 9:
        return pos[1] > lane.sip[1]
    elif l_index == 10:
        return pos[1] > lane.sip[1]
    elif l_index == 11:
        return pos[1] > lane.sip[1]


# Check if car has made it through the intersection
def after_intersection(car):
    lane = car.lane
    l_index = lane.index
    pos = car.position

    # Left lanes
    if l_index == 0:
        return pos[1] > lane.eip[1]
    elif l_index == 1:
        return pos[0] > lane.eip[0]
    elif l_index == 2:
        return pos[1] < lane.eip[1]

    # Bottom lanes
    elif l_index == 3:
        return pos[0] < lane.eip[0]
    elif l_index == 4:
        return pos[1] > lane.eip[1]
    elif l_index == 5:
        return pos[0] > lane.eip[0]

    # Right lanes
    elif l_index == 6:
        return pos[1] < lane.eip[1]
    elif l_index == 7:
        return pos[0] < lane.eip[0]
    elif l_index == 8:
        return pos[1] > lane.eip[1]

    # Top lanes
    elif l_index == 9:
        return pos[0] > lane.eip[0]
    elif l_index == 10:
        return pos[1] < lane.eip[1]
    elif l_index == 11:
        return pos[0] < lane.eip[0]


# Given a car, this function will calculate and return
# the new position  while in the intersection by utilizing
# h is the x position for the center of the circle,
# k is the y position for the center of the circle, and
# r is the radius
# angle is the angle of the turn
def intersection_pos(car):
    lane = car.lane
    x = car.position[0]
    y = car.position[1]
    
    if lane.index == 0:
        h = lane.sip[0]
        k = lane.eip[1]
        r = abs(h - k)
        angle = math.radians(-45)
        omega = .01 + car.vel * .0005

        angle = angle + omega
        x = x + r * omega * math.cos(angle + math.pi / 2)
        y = y + r * omega * math.sin(angle + math.pi / 2)
        return [x,y]
        
    elif lane.index == 1:
        return [x + car.vel, y]

    elif lane.index == 2:
        h = lane.sip[0]
        k = lane.eip[1]
        r = abs(h - k)
        angle = math.radians(70)
        omega = .01 + car.vel * .003

        angle = angle + omega
        x = x - r * omega * math.cos(angle + math.pi / 2)
        y = y - r * omega * math.sin(angle + math.pi / 2)
        return [x,y]
        
    elif lane.index == 3:
        h = lane.sip[1]
        k = lane.eip[0]
        r = abs(h - k)
        angle = math.radians(-57)
        omega = .01 + car.vel * .025

        angle = angle + omega
        x = x - r * omega * math.cos(angle + math.pi / 2)
        y = y + r * omega * math.sin(angle + math.pi / 2)
        #print [x,y]
        return [x,y]

    elif lane.index == 4:
        return [x, y + car.vel]

    elif lane.index == 5:
        h = lane.sip[0]
        k = lane.eip[1]
        r = abs(h - k)
        angle = math.radians(60)
        omega = .01 + car.vel * .0005

        angle = angle + omega
        x = x - r * omega * math.cos(angle + math.pi / 2)
        y = y + r * omega * math.sin(angle + math.pi / 2)
        #print [x, y]
        return [x,y]

    elif lane.index == 6:
        h = lane.sip[0]
        k = lane.eip[1]
        r = abs(h - k)
        angle = math.radians(-50)
        omega = .01 + car.vel * .0005

        angle = angle + omega
        x = x - r * omega * math.cos(angle + math.pi / 2)
        y = y - r * omega * math.sin(angle + math.pi / 2)
        #print [x, y]
        return [x,y]
    
    elif lane.index == 7:
        return [x - car.vel, y]
    
    elif lane.index == 8:
        h = lane.sip[0]
        k = lane.eip[1]
        r = abs(h - k)
        angle = math.radians(-40)
        omega = .01 + car.vel * .03

        angle = angle + omega
        x = x - r * omega * math.cos(angle + math.pi / 2)
        y = y + r * omega * math.sin(angle + math.pi / 2)
        #print [x, y]
        return [x,y]

    elif lane.index == 9:
        h = lane.sip[1]
        k = lane.eip[0]
        r = abs(h - k)
        angle = math.radians(-45)
        omega = .01 + car.vel * .02

        angle = angle + omega
        x = x + r * omega * math.cos(angle + math.pi / 2)
        y = y - r * omega * math.sin(angle + math.pi / 2)
        #print [x, y]
        return [x,y]

    elif lane.index == 10:
        return [x, y - car.vel]

    elif lane.index == 11:
        h = lane.sip[1]
        k = lane.eip[0]
        r = abs(h - k)
        angle = math.radians(-35)
        omega = .01 + car.vel * .0005

        angle = angle + omega
        x = x - r * omega * math.cos(angle + math.pi / 2)
        y = y - r * omega * math.sin(angle + math.pi / 2)
        print [x, y]
        return [x,y]
