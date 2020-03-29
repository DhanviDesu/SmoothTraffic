import math
from car import Car
from traffic import Traffic
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


constTime = 0.05
class Planner:

    def __init__(self,trafficInstance,controller):
        self.trafficInstance = trafficInstance
        self.controller = controller

    def run(self):
        d_err = []
        l_err = []
        time_length = []
        traffic = 0
        while not (self.trafficInstance.missed() or
            self.trafficInstance.reached() or self.trafficInstance.collision()):
            condition, lane_err,dist_err,time = self.trafficInstance.updateAll(constTime)
            currentPos = self.getCarLoc()
            lane,vel = self.controller(currentPos,lane_err,dist_err,constTime)
            if(lane ==0):
                self.trafficInstance.updateOne(True,vel)
            else:
                self.trafficInstance.updateOne(False,lane)
            d_err.append(dist_err)
            l_err.append(lane_err)
            time_length.append(time)
            traffic = condition
        cost = 0.
        if(traffic==2):
            cost = cost + 10000
        if(traffic==1):
            cost = cost - 10000
        if(traffic==3):
            cost = cost + 5000
        for i in range(len(time_length)):
            cost = cost + time_length[i]*10 + l_err[i]*30 + d_err[i]
        return cost,self.trafficInstance.carArray[self.trafficInstance.target].posArray

    def showAll(self):
        return self.trafficInstance.carArray

    def getCarLoc(self):
        current =[]
        for i in range(len(self.trafficInstance.carArray)):
            if(i!=self.trafficInstance.target):
                car = self.trafficInstance.carArray[i]
                current.append((car.x,car.lane))
        return current

if __name__ == '__main__':

        #input layer: traffic instance, lane err, dist err, time
        #ouput layer: change lane, change val
        #neural network

        # trafficInstance: current instance of traffic
        def controller(carLoc, lane_err, dist_err,time):
            changeVel=20
            changeLane=0
    #NEURAL NETWORK
            return changeLane, changeVel

        carArray=[]

        x3 = 0.
        v3 = 80
        lane3 = 0
        car3 = Car(x3,v3,lane3,[(x3,lane3)])
        carArray.append(car3)

        #fourth car collides in lane 0
        x4 = 0.
        v4 = 66
        lane4 = 1
        car4 = Car(x4,v4,lane4,[(x4,lane4)])
        carArray.append(car4)

        bigTraffic = Traffic(carArray,0,(15.,0))
        attempt = Planner(bigTraffic,controller)

        #print(attempt.run())
