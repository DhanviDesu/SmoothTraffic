import math
from car import Car
import random
import matplotlib
import matplotlib.pyplot as plt

#simulate a traffic incident

# target is where you want to get to
class Traffic:
    def __init__(self, carArray,target,targetLoc):
        self.carArray = carArray
        self.target = target
        self.targetLoc = targetLoc
        self.time =0

    # 1 for reached
    # 2 for collision
    def updateAll(self,time):
        self.time = time
        for i in range(len(self.carArray)):
            self.carArray[i].updatePos(time)
            if(i==self.target):
                if(self.reached()):
                    lane_err,dist_err,time = error()
                    return 1,lane_err,dist_err,time
                if(self.missed()):
                    print("Missed")
                    lane_err,dist_err,time = error()
                    return 3,lane_err,dist_err,time
        lane_err,dist_err,time = error()
        if(self.collision()):
            print("Collision occurred")
            return 2,lane_err,dist_err,time
        return 0,lane_err,dist_err,time

    # change is either going to be velocity or lane
    # if true update velocity
    # if false update lane
    def updateOne(self,which,change):
        if(which):
            return self.carArray[self.target].updateVel(change)
        else:
            return self.carArray[self.target].updateLane(change)

    def missed(self):
        if(self.carArray[self.target].x - self.targetLoc[0] > 5):
            return True
        return False

    def reached(self):
        if(self.carArray[self.target].lane == self.targetLoc[1]):
            if(abs(self.carArray[self.target].x - self.targetLoc[0]) <=5):
                return True
        return False

    def collision(self):
        tarCar = self.carArray[self.target]
        for i in range(len(self.carArray)):
            temp = self.carArray[i]
            if(i==self.target):
                pass
            elif(temp.lane == tarCar.lane):
                if(abs(temp.x - tarCar.x)<=0.25):
                    return True
        return False

    # time cost
    # lane difference
    # destination difference
    def error(self):
        lane_err = self.targetLoc[1] - self.carArray[self.target].lane
        dist_err = self.targetLoc[0] - self.carArray[self.target].x
        return lane_err,dist_err,self.time

if __name__ == '__main__':

    carArray=[]

    #first car
    #x1 = 10.
    #v1 = 70
    #lane1 = 3
    #car1 = Car(x1,v1,lane1,[(x1,lane1)])
    #carArray.append(car1)

    #second car
    #x2 = 20.
    #v2 = 65
    #lane2 = 2
    #car2 = Car(x2,v2,lane2,[(x2,lane2)])
    #carArray.append(car2)

    #third car
    x3 = 0.
    v3 = 80
    lane3 = 4
    car3 = Car(x3,v3,lane3,[(x3,lane3)])
    carArray.append(car3)

    #fourth car collides with third car in lane 0
    #x4 = 66
    #lane4 = 0
    #car4 = Car(x4,v4,lane4,[(x4,lane4)])
    #carArray.append(car4)

    #fifth car collides with third car after travelling some distance in lane due to speed differences
    #x5 = 5.
    #v5 = 55
    #lane5 = 0
    #car5 = Car(x5,v5,lane5,[(x5,lane5)])
    #carArray.append(car5)

    #sixth car collides with car 3 in lane 2
    #x6 = 0.
    #v6 = 75
    #lane6 = 2
    #car6 = Car(x6,v6,lane6,[(x6,lane6)])
    #carArray.append(car6)

    #seventh car collides with car 3 in lane 1
    #x7 = 0.
    #v7 = 70
    #lane7 = 1
    #car7 = Car(x7,v7,lane7,[(x7,lane7)])
    #carArray.append(car7)

    #eigth car collides with car 3 in lane 3
    x8 = 0.
    v8 = 75
    lane8 = 3
    car8 = Car(x8,v8,lane8,[(x8,lane8)])
    carArray.append(car8)

    #ninth car so there is a third car to test with
    x9 = 0.
    v9 = 60
    lane9 = 1
    car9 = Car(x9,v9,lane9,[(x9,lane9)])
    carArray.append(car9)

    #tenth car
    x10 = 0.
    v10 = 60
    lane10 = 0
    car10 = Car(x10,v10,lane10,[(x10,lane10)])
    carArray.append(car10)

    #eleventh car
    #x11 = 0.
    #v11 = 80
    #lane11 = 4
    #car11 = Car(x11,v11,lane11,[(x11,lane11)])
    #carArray.append(car11)

    #twelfth car
    #x12 = 20.
    #v12 = 80
    #lane12 = 3
    #car12 = Car(x12,v12,lane12,[(x12,lane12)])
    #carArray.append(car12)

    #together
    # 0 indexed target
    # car 3 is target
    bigTraffic = Traffic(carArray,0,(100.,0))
    for i in range(62):
        bigTraffic.updateOne(False,-1)
        check = bigTraffic.updateAll(0.05)[0]
        if(check ==1):
            bigTraffic.updateOne(True,0)
        elif(check ==2 ):
            break
    #print(bigTraffic.error())
    for car in bigTraffic.carArray:
        xList = []
        laneList = []
        print(len(car.posArray))
        for element in car.posArray:
            xList.append(element[0])
            laneList.append(element[1])

        # y axis is the "lane" and x is distance traveled
        plt.plot(xList, laneList,'o')
    plt.plot(100,0,"X")
    plt.show()
