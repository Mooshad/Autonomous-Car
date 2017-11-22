class car:
    # Initialize car.
    # lane is a lane in the world
    # vel is a 2d vector containing current x and y velocity.
    # acc is a 2d vector containing current x and y acceleration.
    def __init__(self, lane, vel, acc, color):
        self.position = lane.scp
        self.lane = lane
        self.lane_index = lane.index
        self.vel = vel
        self.acc = [0,0]
        self.color = color
        self.time = 0
        
    # On tick, update velocity and acceleration
    def on_tick(self, new_acc):
        self.position[0] = self.position[0] + self.vel[0]
        self.position[1] = self.position[1] + self.vel[1]
        self.vel[0] = self.vel[0] + self.acc[0]
        self.vel[1] = self.vel[1] + self.acc[1]
        self.acc = new_acc
        self.time = self.time + 1

def check_collision(car1, car2):
    pass

    
