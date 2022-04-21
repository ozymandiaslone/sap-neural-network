#imports
import numpy as np
import time
import random
import nnet
import player as p
import gameviewer as g
import interface as itf
import os

#Initialize a variable to store the generation size (needs to be one higher than intended due to indexing)
gen_size = 16

#Initialze a variable to store the players in a generation
gen = []

#Initialize a variable to use during counting
count = 0

#Initialize a variable to store the current game number
game_num = 1

#Initialize a boolean variable to determine whether to evolve the species
evolve = True

'''Define a function which returns the number of brains currently saved to disk'''
def numBrains():

    brain_count = 0

    dir_path = "./neural_data"
    for path in os.listdir(dir_path):
        #Check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            brain_count += 1

    #Return the number of brains         
    return int(brain_count/2)

#If there are brains saved to disk, load them into players
#NO FITNESS LOADING CURRENTLY (But I think heuristically that turns out to be okay, since that information is preserved in the order in which the brains are saved and loaded)
if numBrains() != 0:
    while count + 1 < numBrains():
        i_h_weights = np.load("./neural_data/player"+str(count)+"IH.npy")
        h_o_weights = np.load("./neural_data/player"+str(count)+"HO.npy")
        gen.append(p.Players(0, itf.getGameInfo(0,0), i_h_weights, h_o_weights))
        print("LOADED BRAIN")
        count += 1

#If we haven't loaded enough brains from disk, create random new ones
if count < gen_size:
    for i in range(count,gen_size):
        gen.append(p.Players(0, itf.getGameInfo(0,0)))

count = 0

#Dangerous variable allowing you to start training in the middle of a generation. Only change it if you really mean to.
startnum = 0

#Main loop
while evolve:
    #print(str(len(gen)))
    #For each player in the genration, play a game and update their fitness
    for player in gen:
        if count >= startnum:
            game_num = itf.playGame(player, game_num)
        count += 1
    
    #After the generation has been played, evolve it.
    print("----EVOLVING GENERATION----")
    new_gen = gen[0].evolve_population(gen=gen)

    #Set the active generation to the newly evolved generation
    gen = new_gen

    #Save each new brain to disk
    count = 0
    for player in gen:
        np.save('./neural_data/player'+str(count)+"IH.npy",player.nnet.weight_input_hidden)
        np.save('./neural_data/player'+str(count)+"HO.npy",player.nnet.weight_hidden_output)
        count += 1

    #Reset variables
    count = 0
    game_num = 1
    startnum = 0