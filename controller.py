import math
from car import Car
from traffic import Traffic
from planner import Planner
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

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

N_OUTPUTS = 2
N_INPUTS = 4
N_HIDDEN_UNITS =  # Define here
N_EPOCHS =  # define here

input = tf.placeholder(tf.float32, shape=[None, N_INPUTS], name='input')  # input here

outputs = tf.placeholder(tf.float32, shape=[None, N_OUTPUTS], name='output')  # one sample is something like[Ax,Ay,Az]

# one hidden layer with 3 outputs
W = {
    'hidden': tf.Variable(tf.random_normal([N_INPUTS, N_HIDDEN_UNITS])),
    'output': tf.Variable(tf.random_normal([N_HIDDEN_UNITS, N_OUTPUTS]))
}
biases = {
    'hidden': tf.Variable(tf.random_normal([N_HIDDEN_UNITS], mean=1.0)),
    'output': tf.Variable(tf.random_normal([N_OUTPUTS]), mean=1.0)
}

hidden = tf.matmul(input, W['hidden']) + biases['hidden']  # hidden layer
output_ = tf.matmul(hidden, W['output']) + biases['output']  # outputs

cost = tf.reduce_mean(tf.square(output_ - outputs))  # calculates the cost
optimizer = tf.train.GradientDescentOptimizer(0.001).minimize(cost)  # optimazer

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    for epoch in range(N_EPOCHS):

    # _ = session.run([optimizer],feed_dict={input: , outputs : }) should feed input and output as [Ax,Ay,Az]
