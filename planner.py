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
            self.trafficInstance.reached()): #or self.trafficInstance.collision()):
            condition, lane_err,dist_err,time = self.trafficInstance.updateAll(constTime)
            currentPos = self.getCarLoc()
            lane,vel = self.controller(currentPos,lane_err,dist_err,constTime)
            if(lane ==0):
                self.trafficInstance.updateOne(True,vel)
            else:
                if(lane < 0):
                    self.trafficInstance.updateOne(False,-1)
                else:
                    self.trafficInstance.updateOne(False,1)
            d_err.append(dist_err)
            l_err.append(lane_err)
            time_length.append(time)
            traffic = condition
        cost = 0.
        # if(traffic==2):
        #     cost = cost + 10000
        if(traffic==1):
            cost = cost - 1*10**8
        if(traffic==3):
            cost = cost + 5*10**6
        for i in range(len(time_length)):
            cost = cost + l_err[i]*1000 + d_err[i] #+time_length[i]*10
        return cost,self.trafficInstance.carArray[self.trafficInstance.target].posArray

    def showAll(self):
        return self.trafficInstance.carArray

    # def getCarLoc(self):
    #     current = 0
    #     for i in range(len(self.trafficInstance.carArray)):
    #         lane = abs(self.trafficInstance.carArray[i].lane -
    #                     self.trafficInstance.carArray[self.trafficInstance.target].lane)
    #         if(lane<=1):
    #             car = (self.trafficInstance.carArray[i].x -
    #                 self.trafficInstance.carArray[self.trafficInstance.target].x)**2
    #             lane = (self.trafficInstance.carArray[i].lane -
    #                 self.trafficInstance.carArray[self.trafficInstance.target].lane)**2
    #             current = current + math.sqrt(car+lane)
    #     return current
    def getCarLoc(self):
        lane = (self.trafficInstance.carArray[self.trafficInstance.target].lane - self.trafficInstance.targetLoc[1])**2
        car = (self.trafficInstance.carArray[self.trafficInstance.target].x - self.trafficInstance.targetLoc[0])**2
        return math.sqrt(lane+car)

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
