# -*- coding: utf-8 -*-
"""
Created on Wed May 20 07:59:25 2020

@author: LJ_201718
"""
import random as r
import numpy as np
import agent_fusee as ag

altitude = 10000
speed = 0
throttle = 0
fuel = 1000
gameState = 0

matrice_QL = np.loadtxt('QLdata.txt', dtype=int)

def agentAuto():
    if speed <= 30 or altitude > 6000:
        return 0
    elif speed <= 38:
        return 9
    elif speed >= 40:
        return 19
    else:
        return 10


def environment():
    global altitude
    global speed
    global throttle
    global fuel
    global gameState

    throttle = ag.agentQL()
    if fuel <= 0:
        fuel = 0
        throttle = 0

    a = 9.8-throttle
    altitude -= speed*0.1 - a*0.01/2
    speed += a*0.1
    fuel -= throttle*0.1

    if altitude <= 0:
        if speed <= 40:
            altitude = 0
            throttle = 0
            speed = 0
            gameState = 2
        else:
            altitude = 0
            throttle = 0
            speed = 0
            gameState = 1

def environmentSimple():
    while gameState == 0:
        environment()
    return gameState

winner = environment()
if winner == 1:
    print("Explosion!")
else:
    print("Atterrissage réussi!")