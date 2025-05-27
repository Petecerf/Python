# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as mp
import environnement_fusee as env

QLdata = np.zeros((18,20))

# Matrice de transition -> dimension 20 = sorties possibles de l'agent
#                       -> dimension 18 = état de l'altitude de la fusée

episodesTraining = 1500      # Nombre d'épisodes pour l'entrainemnt
epsilonTraining = 0.15       # Valeur de la variable Epsilon

victoriesTraining = np.zeros(episodesTraining)
for i in range(episodesTraining):
    victoriesTraining[i] = env.environmentQLearning(QLdata, epsilonTraining)

print(QLdata)
np.savetxt('QLdata_test.txt',QLdata,fmt='%d')

episodesTest = 500
epsilonTest = 0

victories = np.zeros(episodesTest)
for i in range(episodesTest):
    victories[i] = env.environmentQLearning(QLdata, epsilonTest)

mp.subplot(211)
mp.plot(victoriesTraining)
mp.subplot(212)
mp.plot(victories)
mp.show()

