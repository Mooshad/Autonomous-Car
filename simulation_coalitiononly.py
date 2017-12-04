import pyglet
from SimObjects import SimObject
from car import *
from lane import lane
from random import *
from copy import deepcopy
from math import *
from CGSolver import *


# This class has everything needed to init and animate our simulation
class SimWindow(pyglet.window.Window):


    # ---------- BEGIN CONSTANT DEFINITIONS ----------
    MAX_VEL = 5 # Maximum velocity
    MAX_ACC = 1 # Maximum acceleration
    MAX_DEC = -1 # Maximum decceleration
    SPAWN_RATE = 20 # A new car will come approximately 1/SPAWN_RATE ticks

    # Car height
    CH = 30
    # Car width
    CW = 42
    
    # Initialize lanes
    # starting car position, intersection start,
    # intersection end, ending car position
    # Need to check later to make sure ending inter and car positions are okay
    lane_0 = lane([0, 482-CH], [300-CW, 482-CH], [518, 700+CH], [518, 1000+CH], 0) # pink left
    lane_1 = lane([0, 415-CH], [300-CW, 415-CH], [700, 415-CH], [1000, 415-CH], 1) # pink straight
    lane_2 = lane([0, 348-CH], [300-CW, 348-CH], [318, 300], [318, 0], 2) # pink right

    lane_3 = lane([518, 0], [518, 300], [300-CW, 585+CW], [0, 585+CW], 3) # green left
    lane_4 = lane([585, 0], [585, 300], [585, 700+CW], [585, 1000+CW], 4) # green straight
    lane_5 = lane([652, 0], [652, 300], [700, 348], [1000, 348], 5) # green right

    lane_6 = lane([1000, 548-CH], [700, 548-CH], [452, 300], [452, 0], 6) # yellow left
    lane_7 = lane([1000, 615-CH], [700, 615-CH], [300-CW, 615-CH], [0, 615-CH], 7) # yellow straight
    lane_8 = lane([1000, 682-CH], [700, 682-CH], [652, 700], [652, 1000+CW], 8) # yellow right

    lane_9 = lane([452, 1000+CW], [452, 700+CW], [700, 485-CH], [1000, 485-CH], 9) # blue left
    lane_10 = lane([385, 1000+CW], [385, 700+CW], [385, 300], [385, 0], 10) # blue straight
    lane_11 =  lane([318, 1000+CW], [318, 700+CW], [300-CW, 682-CH], [0, 682-CH], 11) # blue right
    
    # --------------- END CONSTANT DEFINITONS ----------------
    
    def __init__(self, *args, **kwargs):
        super(SimWindow, self).__init__(*args, **kwargs)
        self.set_location(200, 200) # Set position of window on screen
        self.frame_rate = 1/30.0

        self.background = SimObject(0, 0, 'resources/intersection.png')
        self.loc = []

    # Drawing stuff onto the scene
    # loc - list of car. Each car in the list will be drawn at it's position
    def on_draw(self):
        self.clear()
        self.background.sprite.draw()
        # Draw all cars in loc
        for c in self.loc:
            temp = SimObject(c.position[0], c.position[1], 'resources/'+c.color+'_car.png')
            temp.sprite.rotation = c.rotation
            temp.sprite.draw()

            
    # Update stuff (cars, etc) each tick.
    # Pretty much all the work is doen in here
    def update(self, dt):
        for c in self.loc:
            #


            # GAME THEORY STUFF DONE HERE, CHANGE ACCELERATIONS
            # Coalition Game Start.
            if len(self.loc) != 0:
                cars = []
                [carInC, carNotInC] = [MergeAndSplit(1, 1000, self.loc, 5)[0], MergeAndSplit(1, 1000, self.loc, 5)[1]]
                for cinc in carInC:
                    cinc.on_tick(1)
                for cnotinc in carNotInC:
                    cnotinc.on_tick(-1)
                if len(carInC) != 0:
                    cars.extend(carInC[i] for i in range(len(carInC)))
                if len(carNotInC) != 0:
                    cars.extend(carNotInC[i] for i in range(len(carNotInC)))
                if len(cars) != 0:
                    self.loc = deepcopy(cars)
            # Coalition Game End.

            # Update car's acceleration each tick
            #c.on_tick(0)

        # Randomly generate a new car - TODO: MAKE SURE CARS DONT SPAWN
        # ON TOP OF EACH OTHER
        if(randint(0,self.SPAWN_RATE) == 0):
            lane = randint(0, 11)
            if lane == 0:
                self.loc.append(car(deepcopy(self.lane_0), 'blue'))
            if lane == 1:
                self.loc.append(car(deepcopy(self.lane_1), 'yellow'))
            if lane == 2:
                self.loc.append(car(deepcopy(self.lane_2), 'green'))
            if lane == 3:
                self.loc.append(car(deepcopy(self.lane_3), 'pink'))
            if lane == 4:
                self.loc.append(car(deepcopy(self.lane_4), 'blue'))
            if lane == 5:
                self.loc.append(car(deepcopy(self.lane_5), 'yellow'))
            if lane == 6:
                self.loc.append(car(deepcopy(self.lane_6), 'green'))
            if lane == 7:
                self.loc.append(car(deepcopy(self.lane_7), 'pink'))
            if lane == 8:
                self.loc.append(car(deepcopy(self.lane_8), 'blue'))
            if lane == 9:
                self.loc.append(car(deepcopy(self.lane_9), 'yellow'))
            if lane == 10:
                self.loc.append(car(deepcopy(self.lane_10), 'green'))
            if lane == 11:
                self.loc.append(car(deepcopy(self.lane_11), 'pink'))

            # Make sure addition didn't cause a collision
            for c1 in self.loc:
                if c1.time == 0:
                    for c2 in self.loc:
                        if check_collision(c1,c2) and c1.time != c2.time:
                            self.loc.remove(c1)
                            break
        # Delete out of bound cars and check for collisions
        new_loc = []
        for c1 in self.loc:
            for c2 in self.loc:
                if c1.position != c2.position and check_collision(c1,c2):
                    c1.color = 'red'
                    c2.color = 'red'
            if not check_out_of_bounds(c1):
                new_loc.append(c1)
        self.loc = new_loc


            
if __name__ == "__main__":
        window = SimWindow(1000, 1000, "Test", resizable=False)
        pyglet.clock.schedule_interval(window.update, 1/10) #window.frame_rate
        pyglet.app.run()
        
