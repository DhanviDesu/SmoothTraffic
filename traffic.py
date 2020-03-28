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


    # 1 for reached
    # 2 for collision
    def updateAll(self,time):
        for i in range(len(self.carArray)):
            self.carArray[i].updatePos(time)
            if(i==self.target):
                if(self.reached()):
                    return 1
        if(self.collision()):
            print("Collision occurred")
            return 2

    # change is either going to be velocity or lane
    # if true update velocity
    # if false update lane
    def updateOne(self,which,change):
        if(which):
            return self.carArray[self.target].updateVel(change)
        else:
            return self.carArray[self.target].updateLane(change)

    def reached(self):
        if(self.carArray[self.target].lane == self.targetLoc[1]):
            if(abs(self.carArray[self.target].x - self.targetLoc[0]) <=1):
                return True
        return False

    def collision(self):
        tarCar = self.carArray[self.target]
        for i in range(len(self.carArray)):
            temp = self.carArray[i]
            if(i==self.target):
                pass
            elif(temp.lane == tarCar.lane):
                if(abs(temp.x - tarCar.x)<=0.1):
                    return True
        return False

if __name__ == '__main__':

    carArray=[]

    #first car
    x1 = 10.
    v1 = 70
    lane1 = 3
    car1 = Car(x1,v1,lane1,[(x1,lane1)])
    carArray.append(car1)

    #second car
    x2 = 20.
    v2 = 65
    lane2 = 2
    car2 = Car(x2,v2,lane2,[(x2,lane2)])
    carArray.append(car2)

    #third car
    x3 = 0.
    v3 = 80
    lane3 = 4
    car3 = Car(x3,v3,lane3,[(x3,lane3)])
    carArray.append(car3)

    #fourth car
    x4 = 0.
    v4 = 66
    lane4 = 0
    car4 = Car(x4,v4,lane4,[(x4,lane4)])
    carArray.append(car4)

    #together
    # 0 indexed target
    # car 3 is target
    bigTraffic = Traffic(carArray,2,(100.,0))
    for i in range(62):
        bigTraffic.updateOne(False,-1)
        check = bigTraffic.updateAll(0.05)
        if(check ==1):
            bigTraffic.updateOne(True,0)
        elif(check ==2 ):
            break

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
