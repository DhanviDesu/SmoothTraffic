import math
from car import Car
from traffic import Traffic
from planner import Planner
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def generate_Traffic(cars):
    carArray=[]
    for i in range(cars):
        x = random.randint(0,20)
        v = random.randint(60,80)
        lane = random.randint(0,5)
        carArray.append(Car(x,v,lane,[(x,lane)]))
    target = random.randint(0,cars-1)
    distance = random.randint(0,1000)
    bigTraffic = Traffic(carArray,target,(distance,0))
    return bigTraffic



if __name__ == '__main__':
    def controller(carLoc, lane_err, dist_err,time):
        changeVel=20
        changeLane=0
    #NEURAL NETWORK
        return changeLane, changeVel
    attempt = Planner(generate_Traffic(5),controller)
    attempt.run()

    for car in attempt.showAll():
        xList = []
        laneList = []
        for element in car.posArray:
            xList.append(element[0])
            laneList.append(element[1])

        # y axis is the "lane" and x is distance traveled
        plt.plot(xList, laneList,'o')
    plt.plot(attempt.trafficInstance.targetLoc[0],0,"X")
    plt.show()
