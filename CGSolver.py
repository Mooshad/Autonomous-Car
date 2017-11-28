from car import car
from copy import deepcopy
from random import *
def carInterfere(mycar,othercars):

    numberOfInterfere = 0

    mylane = mycar.lane

    lane0 = [0,1,2,4,5,6,8,11]
    lane1 = [0,1,2,5,7,8,9,11]
    lane2 = [0,1,2,3,4,5,6,7,8,9,10,11]
    lane3 = [2,3,4,5,7,8,9,11]
    lane4 = [0,2,3,4,5,8,10,11]
    lane5 = [0,1,2,3,4,5,6,7,8,9,10,11]
    lane6 = [0,2,5,6,7,8,10,11]
    lane7 = [1,2,3,5,6,7,8,11]
    lane8 = [0,1,2,3,4,5,6,7,8,9,10,11]
    lane9 = [1,2,3,5,8,9,10,11]
    lane10 = [2,4,5,6,8,9,10,11]
    lane11 = [0,1,2,3,4,5,6,7,8,9,10,11]

    for c in othercars:

        otherlane = c.lane

        if mylane == 0 and lane0.count(otherlane)== 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 1 and lane1.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 2 and lane2.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 3 and lane3.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 4 and lane4.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 5 and lane5.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 6 and lane6.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 7 and lane7.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 8 and lane8.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 9 and lane9.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 10 and lane10.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1
        if mylane == 11 and lane11.count(otherlane) == 0:
            numberOfInterfere = numberOfInterfere + 1

    return numberOfInterfere

def Payoff(p,crashPenalty,mycar,othercars):
    n = carInterfere(mycar,othercars)
    if n == 0:
        return 0
    else:
        return crashPenalty * p * n/ (len(othercars) - n)

def MergeAndSplit(p, crashPenalty,carLists,maxIteration):
    CoalitiontoGo = []
    CoalitionNottoGo = []
    # init coalition in a trivial way.
    for c in carLists:
        if Payoff(p,crashPenalty,c,carLists) == 0:
            CoalitiontoGo.append(c)
        else:
            CoalitionNottoGo.append(c)

    currentPayoff = len(CoalitionNottoGo)
    # init best group payoff with init coalition.

    bestPayoff = deepcopy(currentPayoff)
    answer_InCoalition = deepcopy(CoalitiontoGo)
    answer_OutCoalition = deepcopy(CoalitionNottoGo)

    if len(CoalitionNottoGo) == 0:
        return answer_InCoalition,answer_OutCoalition
    else:
        # for merge
        for m in range(maxIteration):
            dumpCoalitiontoGo = deepcopy(CoalitiontoGo)
            dumpCoalitionNottoGo = deepcopy(CoalitionNottoGo)
            # random pick a car to join the coalition.
            ind = randint(0, len(dumpCoalitionNottoGo)-1)
            cartomerge = dumpCoalitionNottoGo[ind]    # potential bug !!!
            dumpCoalitiontoGo.append(cartomerge)
            dumpCoalitionNottoGo.remove(cartomerge)

            currentPayoff = 0
            validCoalition = True
            for cinc in dumpCoalitiontoGo:
                individualpayoff = Payoff(p, crashPenalty, cinc, dumpCoalitiontoGo)
                if individualpayoff > 1:
                    currentPayoff = bestPayoff + 1
                    break
                else:
                    currentPayoff = currentPayoff + individualpayoff
            currentPayoff = currentPayoff + len(dumpCoalitionNottoGo)

            if bestPayoff >= currentPayoff and validCoalition:
                answer_InCoalition = deepcopy(dumpCoalitiontoGo)
                answer_OutCoalition = deepcopy(dumpCoalitionNottoGo)
                bestPayoff = currentPayoff
                CoalitiontoGo = deepcopy(dumpCoalitiontoGo)
                CoalitionNottoGo = deepcopy(dumpCoalitionNottoGo)

        # for split
        for m in range(maxIteration):
            dumpCoalitiontoGo = deepcopy(CoalitiontoGo)
            dumpCoalitionNottoGo = deepcopy(CoalitionNottoGo)
            # random pick a car to split from the coalition.
            ind = randint(0,len(dumpCoalitiontoGo)-1)
            cartomerge = dumpCoalitionNottoGo[ind]    # potential bug !!!
            dumpCoalitiontoGo.remove(cartomerge)
            dumpCoalitionNottoGo.append(cartomerge)

            currentPayoff = 0
            validCoalition = True
            for cinc in dumpCoalitiontoGo:
                individualpayoff = Payoff(p, crashPenalty, cinc, dumpCoalitiontoGo)
                if individualpayoff > 1:
                    currentPayoff = bestPayoff + 1
                    break
                else:
                    currentPayoff = currentPayoff + individualpayoff
            currentPayoff = currentPayoff + len(dumpCoalitionNottoGo)

            if bestPayoff >= currentPayoff and validCoalition:
                answer_InCoalition = deepcopy(dumpCoalitiontoGo)
                answer_OutCoalition = deepcopy(dumpCoalitionNottoGo)
                bestPayoff = currentPayoff
                CoalitiontoGo = deepcopy(dumpCoalitiontoGo)
                CoalitionNottoGo = deepcopy(dumpCoalitionNottoGo)

    return answer_InCoalition,answer_OutCoalition
