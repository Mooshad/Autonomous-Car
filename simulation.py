import pyglet
from SimObjects import SimObject
from car import car
from lane import lane
from random import *
from copy import deepcopy
from math import *

# This class has everything needed to init and animate our simulation
class SimWindow(pyglet.window.Window):


    # ---------- BEGIN CONSTANT DEFINITIONS ----------
    MAX_VEL = 5 # Maximum velocity
    MAX_ACC = 1 # Maximum acceleration
    MAX_DEC = -1 # Maximum decceleration
    SPAWN_RATE = 20 # A new car will come approximately 1/SPAWN_RATE ticks
    
    # Initialize lanes
    # starting car position, intersection start,
    # intersection end, ending car position
    # Need to check later to make sure ending inter and car positions are okay
    lane_0 = lane([0,430], [440, 430], [848,828], [848, 1044], 0) # pink left
    lane_1 = lane([0,360], [440, 360], [1060, 360], [1502, 360], 1) # pink straight
    lane_2 = lane([0,295], [440, 295], [473, 234], [473, 0], 2) # pink right

    lane_3 = lane([855,0], [855, 242], [428, 630], [0, 630], 3) # green left
    lane_4 = lane([930,0], [930, 242], [930, 808], [930, 1044], 4) # green straight
    lane_5 = lane([987,0], [987, 242], [1064, 323], [1502, 323], 5) # green right

    lane_6 = lane([1502,626], [1055, 626], [628, 250], [628, 0], 6) # yellow left
    lane_7 = lane([1502,690], [1055, 690], [448, 690], [0, 690], 7) # yellow straight
    lane_8 = lane([1502,758], [1055, 758], [1005, 789], [1005, 1044], 8) # yellow right

    lane_9 = lane([640,1044], [640, 789], [1055, 439], [1502, 439], 9) # blue left
    lane_10 = lane([575,1044], [575, 789], [575, 250], [575, 0], 10) # blue straight
    lane_11 =  lane([508,1044], [508, 789], [448, 737], [0, 737], 11) # blue right
    
    # --------------- END CONSTANT DEFINITONS ----------------
    
    def __init__(self, *args, **kwargs):
        super(SimWindow, self).__init__(*args, **kwargs)
        self.set_location(200, 200) # Set position of window on screen
        self.frame_rate = 1/30.0

        self.background = SimObject(0, 0, 'resources/road.png')
        self.loc = []

    # Drawing stuff onto the scene
    # loc - list of car. Each car in the list will be drawn at it's position
    def on_draw(self):
        self.clear()
        self.background.sprite.draw()
        # Draw all cars in loc
        for c in self.loc:
            temp = SimObject(c.position[0], c.position[1], 'resources/'+c.color+'_car.png')
            temp.sprite.rotation = degrees(atan2(c.vel[1], c.vel[0]))
            temp.sprite.draw()

            
    # Update stuff (cars, etc) each tick.
    # Pretty much all the work is doen in here
    def update(self, dt):
        for c in self.loc:
            # GAME THEORY STUFF DONE HERE, CHANGE ACCELERATIONS
            # Update car's acceleration each tick
            c.on_tick([0,0])

        # Randomly generate a new car - TODO: MAKE SURE CARS DONT SPAWN
        # ON TOP OF EACH OTHER
        if(randint(0,self.SPAWN_RATE) == 0):
            lane = randint(0, 11)
            vel = randint(1,5)
            if lane == 0:
                self.loc.append(car(deepcopy(self.lane_0), [vel, 0], [0,0], 'blue'))
            if lane == 1:
                self.loc.append(car(deepcopy(self.lane_1), [vel, 0], [0,0], 'yellow'))
            if lane == 2:
                self.loc.append(car(deepcopy(self.lane_2), [vel, 0], [0,0], 'green'))
            if lane == 3:
                self.loc.append(car(deepcopy(self.lane_3), [0, vel], [0,0], 'pink'))
            if lane == 4:
                self.loc.append(car(deepcopy(self.lane_4), [0, vel], [0,0], 'blue'))
            if lane == 5:
                self.loc.append(car(deepcopy(self.lane_5), [0, vel], [0,0], 'yellow'))
            if lane == 6:
                self.loc.append(car(deepcopy(self.lane_6), [-vel, 0], [0,0], 'green'))
            if lane == 7:
                self.loc.append(car(deepcopy(self.lane_7), [-vel, 0], [0,0], 'pink'))
            if lane == 8:
                self.loc.append(car(deepcopy(self.lane_8), [-vel, 0], [0,0], 'blue'))
            if lane == 9:
                self.loc.append(car(deepcopy(self.lane_9), [0, -vel], [0,0], 'yellow'))
            if lane == 10:
                self.loc.append(car(deepcopy(self.lane_10), [0, -vel], [0,0], 'green'))
            if lane == 11:
                self.loc.append(car(deepcopy(self.lane_11), [0, -vel], [0,0], 'pink'))

            
if __name__ == "__main__":
        window = SimWindow(1502, 1044, "Test", resizable=False)
        pyglet.clock.schedule_interval(window.update, window.frame_rate)
        pyglet.app.run()
        
