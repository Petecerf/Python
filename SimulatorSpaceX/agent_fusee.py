# -*- coding: utf-8 -*-

import random as r
import numpy as np


def agentQL(state,QLData,epsilon):
    a = r.random()
    if a < epsilon: # exploration
        action = r.randint(0,19)
    else: #exploitation
        QLMaxPos = np.argmax(QLData,axis=1)
        action = QLMaxPos[int(state)]
    return action   # Valeur de la vitesse



