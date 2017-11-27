# This is a file for strategic game
# There is no assumption on the max speed yet
# No Correlated Equilibium into account, only pure Nash Equilibrium

import numpy as np
import operator
import random


class StGame(object):
	"""docstring for StGame"""

	def __init__(self, crashThreshold):

		self.threshold = crashThreshold  # the threshold of the distance that two cars will collapse inside the threshold


	# To find the cars who will crash the self.car in the next tick
	# circularRout(car) return the position
	def tellCollapse(self, car, others):

		self_nextPosition = circularRout(car)  #circularRout() is a function to return the next position in the next tick
		others_nextPosition = [circularRout(closestCars[i] for i in range(len(closestCars)))]
		crashCars = []
		crashCars.append(car)
		for i in range(len(others_nextPosition)):
			if self.distanceEucleadian(self_nextPosition, others_nextPosition) <= self.threshold:
				crashCars.append(others[i])
		return crashCars
		

	# if there are two cars: (v, v+a) randomly assign to two cars
	# if there are three cars: (v, v+a, v-a) randomly assign to two cars
	# there is no max speed considered. 
	def strategicGame(self, crashCars):
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


	def distanceEucleadian(self, car1, car2):
		return(np.sqrt(np.sum((car1[i]-car2[i])**2 for i in range(len(car1)))))


# a = [1, 1, 2, 3, 4]
# #print('mini indexes =', values.index(min(a)))
# min_index, min_value = min(enumerate(a), key=operator.itemgetter(1))
# print(min_index)



		
