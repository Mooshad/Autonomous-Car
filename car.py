from random import *

class car:
    # Initialize car.
    # lane is a lane in the world
    # vel is a 2d vector containing current x and y velocity.
    # acc is a 2d vector containing current x and y acceleration.
    def __init__(self, lane, acc, color):
        self.position = lane.scp
        self.lane = lane
        self.lane_index = lane.index
        self.acc = [0,0]
        self.color = color
        self.time = 0

        # rand_vel is the velocity
        rand_vel = randint(3,5)

        # Set the velocity based off of lane index
        if lane.index >= 0 and lane.index <= 2:
            self.vel = [rand_vel, 0]
        elif lane.index > 2 and lane.index <= 5:
            self.vel = [0, rand_vel]
        elif lane.index > 5 and lane.index <= 8:
            self.vel = [-rand_vel, 0]
        elif lane.index > 8 and lane.index <= 11:
            self.vel = [0, -rand_vel]
        
    # On tick, update velocity and acceleration
    def on_tick(self, new_acc):
        # Handle case when not in the intersection
        if out_of_intersection(self):
            self.vel[0] = self.vel[0] + self.acc[0]
            self.vel[1] = self.vel[1] + self.acc[1]
            self.position[0] = self.position[0] + self.vel[0]
            self.position[1] = self.position[1] + self.vel[1]
            self.acc = new_acc
            self.time = self.time + 1
        else:
            pass
            

            
def check_collision(car1, car2):
    pass

    
def out_of_intersection(car):
    lane = car.lane
    l_index = lane.index
    pos = car.position

    # Left lanes
    if l_index == 0:
        return pos[0] < lane.sip[0] or pos[1] > lane.eip[1]
    elif l_index == 1:
        return pos[0] < lane.sip[0] or pos[0] > lane.eip[0]
    elif l_index == 2:
        return pos[0] < lane.sip[0] or pos[1] < lane.eip[1]

    # Bottom lanes
    elif l_index == 3:
        return pos[1] < lane.sip[1] or pos[0] < lane.eip[0]
    elif l_index == 4:
        return pos[1] < lane.sip[1] or pos[1] > lane.eip[1]
    elif l_index == 5:
        return pos[1] < lane.sip[1] or pos[0] > lane.eip[0]

    # Right lanes
    elif l_index == 6:
        return pos[0] > lane.sip[0] or pos[1] < lane.eip[1]
    elif l_index == 7:
        return pos[0] > lane.sip[0] or pos[0] < lane.eip[0]
    elif l_index == 8:
        return pos[0] > lane.sip[0] or pos[1] > lane.eip[1]

    # Top lanes
    elif l_index == 9:
        return pos[1] > lane.sip[1] or pos[0] > lane.eip[0]
    elif l_index == 10:
        return pos[1] > lane.sip[1] or pos[1] < lane.eip[1]
    elif l_index == 11:
        return pos[1] > lane.sip[1] or pos[0] < lane.eip[0]
