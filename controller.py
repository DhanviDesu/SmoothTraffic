import math
from car import Car
from traffic import Traffic
from planner import Planner
import random
from numpy.random import rand
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from cma import fmin2
from multiprocessing import Pool
from numpy import pi, tanh, array, dot
import numpy
import sys

N_TRAIN_TRAFFIC = 10
N_NEURONS = 10
VELOCITY = 1
CARS = 5

def generate_Traffic(cars):
    carArray=[]
    for i in range(cars):
        x = random.randint(0,20)
        v = random.randint(60,80)
        lane = random.randint(0,5)
        carArray.append(Car(x,v,lane,[(x,lane)]))
    target = random.randint(0,cars-1)
    distance = random.randint(0,750)
    bigTraffic = Traffic(carArray,target,(distance,0))
    return bigTraffic

def generateMultiple():
    manyTraffic = []
    for i in range(N_TRAIN_TRAFFIC):
        manyTraffic.append(generate_Traffic(CARS))
    return manyTraffic

def plsWork(args):
    x,traffic= args
    controller = NN(x).controller
    attempt = Planner(traffic,controller)
    return attempt.run()[0]

class NN:

    def __init__(self,x):
        h = (len(x)-1)//4
        self.weight_1 = x[0:h]
        self.weight_0_d = x[h:2*h]
        self.weight_0_t = x[2*h:3*h]
        self.bias_0 = x[3*h:4*h]
        self.bias_1_0 = x[4*h]

    def controller(self,carLoc,lane_err,dist_err,time):
        changeVel = tanh(dot(self.weight_1, tanh(
            (self.weight_0_d * carLoc)+(
                self.weight_0_t * time))+self.bias_0) + self.bias_1_0)
        changeLane = numpy.maximum(0,dot(self.weight_1, tanh(
            (self.weight_0_d * lane_err)+(
                self.weight_0_t * dist_err))+self.bias_0) + self.bias_1_0)
        # changeVel = tanh(dot(self.weight_1, tanh(
        #     (self.weight_0_d * lane_err)+(
        #         self.weight_0_t * time))+self.bias_0) + self.bias_1_0)
        return changeVel,changeLane


if __name__ == '__main__':
    pool = Pool()
    instances = generateMultiple()

    def objective(x, v):
            controller = NN(x).controller
            trackers = []
            for traffic in instances:
                trackers.append([x,traffic])
            costs = pool.map(plsWork,trackers)
            return max(costs)

    x = 2*rand(1,4*N_NEURONS+1)[0]-1
    res = fmin2(objective,
                        x,
                        .5,
                        args=(VELOCITY, ),
                        options={'popsize': 256,
                                'bounds': [-1, 1],
                                'maxiter': 256}) # 5th is mean of final sample distribution
    res=res[1].result[0]
    controller = NN(res).controller

    work = Planner(instances[0],controller)
    work.run()
    #print(work.run()[1])
    for car in work.showAll():
        xList = []
        laneList = []
        for element in car.posArray:
            xList.append(element[0])
            laneList.append(element[1])

        # y axis is the "lane" and x is distance traveled
        plt.plot(xList, laneList,'o')
    plt.plot(work.trafficInstance.targetLoc[0],0,"X")
    plt.show()
    res = res.tolist()
    f = open("reach.txt","w+")
    f.write(str(res))
    f.close()
