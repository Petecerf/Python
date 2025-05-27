# -*- coding: utf-8 -*-

import agent_fusee as ag
import numpy as np
import random as r

#Matricule = LA161349

def environmentQLearning(QLData, epsilon):

    altitude = 10000 - (16 * 100)  # Altitude de départ = 8400
    speed = 49 * 4  # Vitesse de départ = 196
    throttle = 0
    fuel = 1000
    gameState = 0

    positiveReward = 20  # Récompense en cas de succès
    negativeReward = -20  # Pénalité en cas d'échec
    discountFactor = 1  # Facteur d'escompte

    log = np.empty((0, 2))  # Enregistre les décisions de l'agentQL

    while gameState == 0:

        # On évalue d'abord l'état de la fusée et on le met à jour
        state = altitude//2000
        if state > 5:
            state = 5
        if speed < 0:
            state2 = 0
        elif speed > 40:
            state2 = 1
        else:
            state2 = 2

        state += state2*6

        # On envoie l'état à l'agentQL et celui-ci renc
        throttle = ag.agentQL(state, QLData, epsilon)
        log = np.concatenate((log, np.array([[state, throttle]])))

        if fuel <= 0:
            fuel = 0
            throttle = 0

        a = 9.8-throttle
        altitude -= speed*0.1 - a*0.01/2
        speed += a*0.1
        fuel -= throttle*0.1

        # On évalue si l'atterissage est réussi ou non
        if altitude <= 0:
            if speed <= 40:
                altitude = 0
                throttle = 0
                speed = 0
                gameState = 2   # Victoire
                reward = positiveReward
            else:
                altitude = 0
                throttle = 0
                speed = 0
                gameState = 1   # Défaite
                reward = negativeReward

        # Implémentation de l'équation de Bellman
        if gameState != 0:
            for i in range(log.shape[0]):
                a = log.shape[0]-1-i
                QLData[int(log[a,0]), int(log[a,1])] += reward
                reward *= discountFactor

    return gameState


