from car import car
from CGSolver import *

def main():
    # parameters to choose.
    p = 0.001                   # probability to crash with one other cars.
    crashPenalty = 1000         # penalty to crash with one other cars.
    t = 1                       # frame number to update.
    distancethresh = 0.1        # threshold in distance, to consider as possible to crash.

