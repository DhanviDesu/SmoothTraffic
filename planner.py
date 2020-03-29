import math
from car import Car
from traffic import Traffic
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


constTime = 0.05
# neural network with backpropogation
class Planner:

    def __init__(self,trafficInstance,controller):
        self.trafficInstance = trafficInstance
        self.controller = controller

    def run(self):
        d_err = []
        l_err = []
        time_length = []
        traffic
        while not trafficInstance.missed() or trafficInstance.reached() or trafficInstance.collision():
            condition, lane_err,dist_err,time = trafficInstance.updateAll(constTime)
            lane,vel = controller(trafficInstance,lane_err,dist_err,constTime)
            if(lane ==0):
                self.trafficInstance.updateOne(True,vel)
            else:
                self.trafficInstance.updateOne(False,lane)
            d_err.append(dist_err)
            l_err.append(lane_err)
            time_length.append(time)
            traffic = condition
        cost = 0
        if(traffic==2):
            cost = cost + 1000
        if(traffic==1):
            cost = cost - 1000
        if(traffic==3):
            cost = cost + 500
        for i in range(len(time_length)):
            cost = cost + time_length[i]*10 + l_err[i]*30
    #input layer: traffic instance, lane err, dist err, time
    #ouput layer: change lane, change val
    #neural network

    # trafficInstance: current instance of traffic
    def controller(self,trafficInstance, lane_err, dist_err,time):
#NEURAL NETWORK
        return changeLane, changeVel


if __name__ == '__main__':
