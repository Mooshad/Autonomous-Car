# This is a file for strategic game
# There is no assumption on the max speed yet
# No Correlated Equilibium into account, only pure Nash Equilibrium

import numpy as np
import operator
import random


DIS_THRESHOLD = 5

class StGame(object):
	"""docstring for StGame"""

	def __init__(self, crashThreshold):

		self.threshold = crashThreshold  # the threshold of the distance that two cars will collapse inside the threshold


	# To find the cars who will crash the self.car in the next tick
	# circularRout(car) return the position
def tellCollapse(car, others):

	# temp_car = deepcopy(car)
	# temp_others_cars = deepcopy(others)
	# self_nextPosition = temp_car.on_tick(new_acc)  #circularRout() is a function to return the next position in the next tick
	# others_nextPosition = [circularRout(closestCars[i] for i in range(len(closestCars)))]
	crashCars = []
	crashCars.append(car)
	for i in range(len(others)):
		if distanceEucleadian(car, others[i])<= DIS_THRESHOLD :
			crashCars.append(others[i])
	if len(crashCars)>1:
		return crashCars
	else:
		return []
	
		

	# if there are two cars: (v, v+a) randomly assign to two cars
	# if there are three cars: (v, v+a, v-a) randomly assign to two cars
	# there is no max speed considered. 
def strategicGame(crashCars):
	if len(crashCars) == 3:
		sol = [-1, 0, 1]
		random.shuffle(sol)
		return (sol)
	elif len(crashCars) == 2:
		sol = [0, 1]
		random.shuffle(sol)
		return (sol)
	else:
		return (None)



def distanceEucleadian(car1, car2):
	
	return(np.sqrt(np.sum((car1[i]-car2[i])**2 for i in range(len(car1)))))


# a = [1, 1, 2, 3, 4]
# #print('mini indexes =', values.index(min(a)))
# min_index, min_value = min(enumerate(a), key=operator.itemgetter(1))
# print(min_index)



		
