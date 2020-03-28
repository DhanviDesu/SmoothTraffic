import math
import matplotlib
import matplotlib.pyplot as plt

#location of car

class Car:

    def __init__(self,x,v,lane,posArray):
        self.x = x
        self.v = v
        self.lane = lane
        self.posArray = posArray

    def updatePos(self, time):
        self.x = self.v * time + self.x
        self.posArray.append((self.x,self.lane))

    def updateVel(self, velocity):
        self.v = velocity
        return self.v

    #assume 5 lane highway so lane: 0 - 4
    def updateLane(self, value):
        if(self.lane + value < 0 ):
            return self.lane
        elif(self.lane + value > 4):
            return self.lane

        self.lane = self.lane + value
        if(self.lane == 0):
            self.updateVel(60)
        elif(self.lane == 1):
            self.updateVel(65)
        elif(self.lane == 2):
            self.updateVel(70)
        elif(self.lane == 3):
            self.updateVel(75)
        elif(self.lane == 4):
            self.updateVel(80)
        return self.lane

if __name__ == '__main__':

    # x is position
    # v is velocity
    # lane is which lane it is on (restrict from 0-4)
    x_init = 0
    v_init = 60
    lane = 0
    xList = [x_init]
    laneList = [lane]
    dis = Car(x_init, v_init,lane,[(x_init,lane)])

    #update 1 tic
    for i in range(10):
        dis.updatePos(1)

    dis.updateLane(1)

    for i in range(10):
        dis.updatePos(1)

    dis.updateLane(3)

    for i in range(10):
        dis.updatePos(1)

    dis.updateLane(-1)

    for i in range(15):
        dis.updatePos(1)

    #print(dis.posArray)

    for element in dis.posArray:
        xList.append(element[0])
        laneList.append(element[1])

    # y axis is the "lane" and x is distance traveled
    plt.plot(xList, laneList, '-o')
    plt.show()
