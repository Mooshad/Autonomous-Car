from car import car

def CrashDetect(mycar, othercars,t,distancethresh):
    numberOfCarsMayCrash = 0
    myposition = [0, 0]
    otherposition = [0, 0]
    myposition[0] = mycar.position[0] + t * car.vel[0]
    myposition[1] = mycar.position[1] + t * car.vel[1]
    for c in othercars:
        otherposition[0] = c.position[0] + t * c.vel[0]
        otherposition[1] = c.position[1] + t * c.vel[1]
        dist = ((myposition[0] - otherposition[0]) ** 2 + (myposition[1] - otherposition[1]) ** 2) ** 0.5
        if dist >= distancethresh: numberOfCarsMayCrash += 1
    return numberOfCarsMayCrash

def Payoff(p, crashPenalty, mycar, othercars, t, distancethresh):
    n = CrashDetect(mycar, othercars, t, distancethresh)
    if len(othercars) != 0:
        return mycar.tt
    else:
        return mycar.tt + crashPenalty * p * (n-1) / (len(othercars) - n-1)

def MergeAndSplit(p, crashPenalty,carLists,t,distancethresh):
    GtoAcc = []
    GtoAcc = []

    for carind in range(0,len(carLists)):
        mycar = carLists[carind]
        payoffvector[carind] = Payoff(p,crashPenalty,mycar,carLists,t,distancethresh)

    return 0
