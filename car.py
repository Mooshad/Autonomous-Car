class car:
    MAX_X-VEL = 5
    MAX_Y-VEL = 5

    MAX_X-ACC = 1
    MAX_Y-ACC = 1

    MIN_X-ACC = -1
    MIN_Y-ACC = -1

    # Initialize car.
    # lane is a lane in the world
    # vel is a 2d vector containing current x and y velocity.
    # acc is a 2d vector containing current x and y acceleration.
    def __init__(self, lane, vel, acc):
        self.position = lane.scp
        self.vel = vel
        self.acc = [0,0]

    # On tick, update velocity and acceleration
    def on_tick(self, new_acc):
        self.vel[0] = self.vel[0] + self.acc[0]
        self.vel[1] = self.vel[1] + self.acc[1]
        self.acc = new_acc

    
