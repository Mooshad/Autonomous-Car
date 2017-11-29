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
            self.last_position = self.position
            self.position = intersection_pos(self)
        
        self.acc = new_acc
        self.time = self.time + 1

# Check if car has left the simulation area
def check_out_of_bounds(car):
    lane = car.lane
    if lane.index == 11 or lane.index == 7 or lane.index == 3:
        return car.position[0] < -42
    elif lane.index == 2 or lane.index == 10 or lane.index == 6:
        return car.position[1] < 0
    elif lane.index == 9 or lane.index == 1 or lane.index == 5:
        return car.position[0] > 1000
    elif lane.index == 0 or lane.index == 4 or lane.index == 8:
        return car.position[1] > 1042

def check_collision(car1, car2):
    CH = 30
    CW = 42

    pos1 = car1.position
    pos2 = car2.position

    box1_min = [pos1[0], pos1[1]]
    box1_max = [pos1[0] - CW, pos1[1] - CH]
    box2_min = [pos2[0], pos2[1]]
    box2_max = [pos2[0] - CW, pos2[1] - CH]
    
    return box1_max[0] <= box2_min[0] and box2_max[0] <= box1_min[0] and box1_max[1] <= box2_min[1] and box2_max[1] <= box1_min[1]
    

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
        
    if lane.index == 1:
        return [x + car.vel, y]

    elif lane.index == 4:
        return [x, y + car.vel]
    
    elif lane.index == 7:
        return [x - car.vel, y]

    elif lane.index == 10:
        return [x, y - car.vel]

    else:
        p1 = lane.sip
        p2 = lane.eip
        m = (float(p2[1] - p1[1]))/float((p2[0] - p1[0]))

        if lane.index == 0 or lane.index == 2 or lane.index == 5 or lane.index == 9:
            x = x + car.vel
            y = m * car.vel + y
            
        elif lane.index == 3 or lane.index == 8:
            x = m * car.vel + x
            y = y + car.vel
            pass
        elif lane.index == 6 or lane.index == 11:
            x = x - car.vel
            y = y - m * car.vel
        return [x,y]
