import pyglet
from SimObjects import SimObject
from car import car
from lane import lane
from random import *
from copy import deepcopy

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
    lane_0 = lane([0,439], [448, 439], [866,789], [866, 1044]) # pink left
    lane_1 = lane([0,369], [448, 369], [1055, 369], [1502, 369]) # pink straight
    lane_2 = lane([0,299], [448, 299], [494, 299], [494, 0]) # pink right

    lane_3 = lane([865,0], [865, 250], [448, 606], [0, 606]) # green left
    lane_4 = lane([935,0], [935, 250], [935, 787], [935, 1044]) # green straight
    lane_5 = lane([1005,0], [1005, 250], [1055, 299], [1502, 299]) # green right

    lane_6 = lane([1502,606], [1055, 606], [628, 250], [628, 0]) # yellow left
    lane_7 = lane([1502,670], [1055, 670], [448, 670], [0, 670]) # yellow straight
    lane_8 = lane([1502,738], [1055, 738], [1005, 789], [1005, 1044]) # yellow right

    lane_9 = lane([625,1044], [625, 789], [1055, 439], [1502, 439]) # blue left
    lane_10 = lane([560,1044], [560, 789], [560, 250], [560, 0]) # blue straight
    lane_11 =  lane([492,1044], [492, 789], [448, 737], [0, 737]) # blue right
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
        
