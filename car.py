import math
import matplotlib
import matplotlib.pyplot as plt

#location of car

class Car:

    def __init__(self,x,v,lane):
        self.x = x
        self.v = v
        self.lane = lane

    def updatePos(self, time):
        self.x = self.v * time + self.x
        return self.x, self.lane

    def updateVel(self, velocity):
        self.v = velocity
        return self.v

    def updateLane(self, value):
        self.lane = self.lane + value
        return self.lane
        
if __name__ == '__main__':

    # x is position
    # v is velocity
    # lane is which lane it is on (restrict from 1-5)
    x_init = 0
    v_init = 1.
    lane = 0
    xList = [x_init]
    laneList = [lane]
    dis = Car(x_init, v_init,lane)
    
    for i in range(10):
        x, y = dis.updatePos(10)
        xList.append(x)
        laneList.append(y)
        
    dis.updateLane(1)
    
    for i in range(10):
        x, y = dis.updatePos(10)
        xList.append(x)
        laneList.append(y)

    dis.updateLane(1)
    
    for i in range(10):
        x, y = dis.updatePos(10)
        xList.append(x)
        laneList.append(y)

    dis.updateLane(-1)
    
    for i in range(15):
        x, y = dis.updatePos(10)
        xList.append(x)
        laneList.append(y)

    # y axis is the "lane" and x is distance traveled
    plt.plot(xList, laneList, '-o')
    plt.show()
