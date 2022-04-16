'''Imports'''
import pyautogui
import nnet
import player as p
import gameviewer as g 
import time
import random
import numpy as np
import os

'''Global Variables'''
freeze_slot = None
sell_slot = None
buy_slot_one = None
buy_slot_two = None
buy_slot_three = None
buy_slot_four = None
buy_slot_five = None
playing = False

'''Animal names paired corresponding to their respective neuron activation input value'''
animal_keys = [["ant",0.01],
                ["cricket",0.02],
                ["duck",0.03],
                ["fish",0.04],
                ["horse",0.05],
                ["mosquito",0.06],
                ["otter",0.07],
                ["pig",0.08],
                ["crab",0.09],
                ["dodo",0.10],
                ["dog",0.11],
                ["elephant",0.12],
                ["flamingo",0.13],
                ["hedgehog",0.14],
                ["peacock",0.15],
                ["rat",0.16],
                ["shrimp",0.17],
                ["spider",0.18],
                ["badger",0.19],
                ["blowfish",0.20],
                ["camel",0.21],
                ["giraffe",0.22],
                ["kangaroo",0.23],
                ["ox",0.24],
                ["rabbit",0.25],
                ["sheep",0.26],
                ["snail0",0.27],
                ["turtle",0.28],
                ["whale",0.29],
                ["bison",0.30],
                ["deer",0.31],
                ["dolphin",0.32],
                ["hippo",0.33],
                ["monkey",0.34],
                ["penguin",0.35],
                ["rooster",0.36],   
                ["skunk",0.37],
                ["squirrel",0.38],
                ["worm",0.39],
                ["cow",0.40],
                ["crocodile",0.41],
                ["parrot",0.42],
                ["rhino",0.43],
                ["scorpion",0.44],
                ["seal",0.45],
                ["shark",0.46],
                ["turkey",0.47],
                ["cat",0.48],
                ["dragon",0.49],
                ["fly",0.50],
                ["gorilla",0.51],
                ["leopard",0.52],
                ["mammoth",0.53],
                ["snake",0.54],
                ["tiger",0.55],
                ["boar",0.56],
                ["beaver",0.57],
]

'''Define game action functions. These functions perform the actual mouse inputs needed to play the game'''
#Clicks the "Start Arena" button
def startArena():
    pyautogui.click(x=600, y=300)

#Clicks the "Roll" button; if not in a recursive call, set rollbool to True
def roll():
    pyautogui.click(x=200, y=1000)

#Clicks inventory slot one
def clickSlotOne():
    pyautogui.click(x=500, y=700)

#Clicks inventory slot two
def clickSlotTwo():
    pyautogui.click(x=700, y=700)

#Clicks inventory slot three
def clickSlotThree():
    pyautogui.click(x=840, y=700)

#Clicks inventory slot four
def clickSlotFour():
    pyautogui.click(x=1000, y=700)

#Clicks inventory slot five
def clickSlotFive():
    pyautogui.click(x=1122, y=700)

#Clicks the freeze button 
def freeze():
    pyautogui.click(x=1000, y=1000)

#Clicks slot one on the game board
def placeSlotOne():
    pyautogui.click(x=550, y=350)

#Clicks slot two on the game board
def placeSlotTwo():
    pyautogui.click(x=700, y=350)

#Clicks slot three on the game board
def placeSlotThree():
    pyautogui.click(x=810, y=350)

#Clicks slot four on the game board
def placeSlotFour():
    pyautogui.click(x=950, y=350)

#Clicks slot five on the game board
def placeSlotFive():
    pyautogui.click(x=1100, y=350)

#Clicks the end turn button
def endTurn():
    pyautogui.click(x=1500,y=1000)

'''Function to get the current animals lined up in the inventory board. Currently limited by the capabilities
    of the functions within gameviewer.py'''
def getGameInfo(turn):
    board = []
    animals = g.checkForAnimals(g.sliceImage(turn))
    for a1 in animals:
        for a2 in animal_keys:
            if a1 == a2[0]:
                board.append(a2[1])
    while len(board) < 5:
        board.append(0)
    return board

'''Function which takes in an action command, and performs the corresponding action'''
def doAction(action_command, recursive_call):
    global freeze_slot
    global sell_slot
    global buy_slot_one
    global buy_slot_two
    global buy_slot_three
    global buy_slot_four
    global buy_slot_five
    '''These actions are performed based off of a system where an integer number
    between from 0-7 is passed, representing 8 possible general actions, and then 
    clarifying data is inferred from the number loaded into the global variables'''
    
    #Action command 0 Signifies that it wants to freeze or un-freeze one of the inventory slots
    if action_command == 0:
        if freeze_slot == 0:
            clickSlotOne()
            time.sleep(0.3)
            freeze()
        elif freeze_slot == 1:
            clickSlotTwo()
            time.sleep(0.3)
            freeze()
        elif freeze_slot == 2:
            clickSlotThree()
            time.sleep(0.3)
            freeze()
        elif freeze_slot == 3:
            clickSlotFour()
            time.sleep(0.3)
            freeze()
        elif freeze_slot == 4:
            clickSlotFive()
            time.sleep(0.3)
            freeze()
    
    #Action command one signifies that it wants to sell an animal
    elif action_command == 1:
        if sell_slot == 5:
            placeSlotOne()
            time.sleep(0.3)
            freeze()
        if sell_slot == 6:
            placeSlotTwo()
            time.sleep(0.3)
            freeze()
        if sell_slot == 7:
            placeSlotThree()
            time.sleep(0.3)
            freeze()
        if sell_slot == 8:
            placeSlotFour()
            time.sleep(0.3)
            freeze()
        if sell_slot == 9:
            placeSlotFive()
            time.sleep(0.3)
            freeze()
    
    #Action command 2 signifies that it wants to buy the animal in slot 1
    elif action_command == 2:
        if buy_slot_one == 10:
            clickSlotOne()
            time.sleep(0.3)
            placeSlotOne()
        elif buy_slot_one == 11:
            clickSlotOne()
            time.sleep(0.3)
            placeSlotTwo()
        elif buy_slot_one == 12:
            clickSlotOne()
            time.sleep(0.3)
            placeSlotThree()
        elif buy_slot_one == 13:
            clickSlotOne()
            time.sleep(0.3)
            placeSlotFour()
        elif buy_slot_one == 14:
            clickSlotOne()
            time.sleep(0.3)
            placeSlotFive()
    
    #Action command 3 signifies that it wants to buy the animal in slot 2
    elif action_command == 3:
        if buy_slot_two == 15:
            clickSlotTwo()
            time.sleep(0.3)
            placeSlotOne()
        elif buy_slot_two == 16:
            clickSlotTwo()
            time.sleep(0.3)
            placeSlotTwo()
        elif buy_slot_two == 17:
            clickSlotTwo()
            time.sleep(0.3)
            placeSlotThree()
        elif buy_slot_two == 18:
            clickSlotTwo()
            time.sleep(0.3)
            placeSlotFour()
        elif buy_slot_two == 19:
            clickSlotTwo()
            time.sleep(0.3)
            placeSlotFive()
    
    #Action command 4 signifies that it wants to buy the animal in slot 3
    elif action_command == 4:
        if buy_slot_three == 20:
            clickSlotThree()
            time.sleep(0.3)
            placeSlotOne()
        elif buy_slot_three == 21:
            clickSlotThree()
            time.sleep(0.3)
            placeSlotTwo()
        elif buy_slot_three == 22:
            clickSlotThree()
            time.sleep(0.3)
            placeSlotThree()
        elif buy_slot_three == 23:
            clickSlotThree()
            time.sleep(0.3)
            placeSlotFour()
        elif buy_slot_three == 24:
            clickSlotThree()
            time.sleep(0.3)
            placeSlotFive()
    
    #Action command 5 signifies it wants to buy the animal in slot 4
    elif action_command == 5:
        if buy_slot_four == 25:
            clickSlotFour()
            time.sleep(0.3)
            placeSlotOne()
        elif buy_slot_four == 26:
            clickSlotFour()
            time.sleep(0.3)
            placeSlotTwo()
        elif buy_slot_four == 27:
            clickSlotFour()
            time.sleep(0.3)
            placeSlotThree()
        elif buy_slot_four == 28:
            clickSlotFour()
            time.sleep(0.3)
            placeSlotFour()
        elif buy_slot_four == 29:
            clickSlotFour()
            time.sleep(0.3)
            placeSlotFive()
    
    #Action command 6 signifies it wants to buy the animal in slot 5
    elif action_command == 6:
        if buy_slot_five == 30:
            clickSlotFive()
            time.sleep(0.3)
            placeSlotOne()
        elif buy_slot_five == 31:
            clickSlotFive()
            time.sleep(0.3)
            placeSlotTwo()
        elif buy_slot_five == 32:
            clickSlotFive()
            time.sleep(0.3)
            placeSlotThree()
        elif buy_slot_five == 33:
            clickSlotFive()
            time.sleep(0.3)
            placeSlotFour()
        elif buy_slot_five == 34:
            clickSlotFive()
            time.sleep(0.3)
            placeSlotFive()
    
    #If the action command is 7, all it needs to do is click the roll button
    elif action_command == 7:
        roll()
        time.sleep(0.3)

        #If we rolled, we need to return True
        return True

    return False
    
'''Function which takes in a player object, and game number. Plays a single round,
    querying the neural network for decision making, and doing some processing 
    of the return from the net.'''
def playRound(player, game_num, turn, recursive_call):

    #Global variables are used to carry data about the neural network's choices, and check for recursion
    global freeze_slot
    global sell_slot
    global buy_slot_one
    global buy_slot_two
    global buy_slot_three
    global buy_slot_four
    global buy_slot_five
    global playing

    #Initialize an empty list to hold neuron activations representing actions to be taken to be taken during the round
    activations = [None] * 8

    #Initialize an empty list to hold actions to be taken during the turn
    actions = []

    #Initialize an empty "highest value" variable to hold high values in our loops
    high_val = 0

    #Initialize an empty list to hold the paired activation values and the corresponding action
    paired_activations = []

    #initialize a variable to store the potential amount of actions the player is allowed to complete per turn
    max_actions = 7

    #Initialize a variable to store the activation threshold
    activation_threshold = 0.8

    #Initialize a variable to hold the amount of gold we have
    gold = 0

    #Initialize private rollbool, False by default
    rollbool = False

    #If the player is not playing, then it will return
    if not playing:
        return game_num

    #If the player is playing, then it will continue
    if playing:

        #Print the game number if not in recursive call
        if not recursive_call:
            print("Game Number: " + str(game_num))

        #Check if we can see animals in our inventory, if not, attempt to click the "Start Arena" button
        while getGameInfo(turn)[0]==0 and getGameInfo(turn)[1]==0 and getGameInfo(turn)[2]== 0 and g.checkMoney(g.sliceMoney()) == None:
            print("Couldn't see any animals or gold!") 
            startArena()
            time.sleep(0.5)

        #Now that we can see some animals, we query the network for actions
        raw_actions = player.query(getGameInfo(turn))
        for ra in raw_actions:
            actions.append(ra[0])

        #Make sure the freeze slot is empty, then fill it with the correct value
        freeze_slot = None
        for i in range(0,4):
            if actions[i] > high_val:
                high_val = actions[i]
                freeze_slot = i
                activations[0] = actions[i]

        #Reset the high_val, make sure the sell slot is empty, then fill it with the correct value
        high_val = 0
        sell_slot = None
        for i in range(5,9):
            if actions[i] > high_val:
                high_val = actions[i]
                sell_slot = i
                activations[1] = actions[i]

        #Reset the high_val, make sure the buy slot one is empty, then fill it with the correct value
        high_val = 0
        buy_slot_one = None
        for i in range(10,14):
            if actions[i] > high_val:
                high_val = actions[i]
                buy_slot_one = i
                activations[2] = actions[i]

        #Reset the high_val, make sure the buy slot two is empty, then fill it with the correct value
        high_val = 0
        buy_slot_two = None
        for i in range(15,19):
            if actions[i] > high_val:
                high_val = actions[i]
                buy_slot_two = i
                activations[3] = actions[i]

        #Reset the high_val, make sure the buy slot three is empty, then fill it with the correct value
        high_val = 0
        buy_slot_three = None
        for i in range(20,24):
            if actions[i] > high_val:
                high_val = actions[i]
                buy_slot_three = i
                activations[4] = actions[i]

        #Reset the high_val, make sure the buy slot four is empty, then fill it with the correct value
        high_val = 0
        buy_slot_four = None
        for i in range(25,29):
            if actions[i] > high_val:
                high_val = actions[i]
                buy_slot_four = i
                activations[5] = actions[i]

        #Reset the high_val, make sure the buy slot five is empty, then fill it with the correct value
        high_val = 0
        buy_slot_five = None
        for i in range(30,34):
            if actions[i] > high_val:
                high_val = actions[i]
                buy_slot_five = i
                activations[6] = actions[i]
        #Set the roll activation
        activations[7] = actions[35]

        #Associate the activations with the actions, then sort that list in descending order
        for i in range(0,len(activations)):
            paired_activations.append((activations[i],i))
        paired_activations.sort(reverse=True)

        #Print the activations to the console
        print("Paired activations: " + str(paired_activations))

        #Loop thorough every potential action
        for i in range(0,max_actions):
            #Check if the activation amount is above the minimum threshold 
            if paired_activations[i][1] > activation_threshold:
                rolled = doAction(paired_activations[i][1], recursive_call)
                #If we rolled, we need to set the variable accordingly
                if rolled:
                    rollbool = True
                time.sleep(1)

        #Make sure we can see the amount of gold we have
        while g.checkMoney(g.sliceMoney()) == None:
            print("Couldn't see money! Waiting...")
            time.sleep(1)

        #Since we can see a gold value, set the variable
        gold = g.checkMoney(g.sliceMoney())

        #If we are out of gold, set rollbool to false in order to prevent it from playing again
        if gold == 0:
            rollbool = False

        #If we have rolled, we need to play the turn again, but this time recursively
        if rollbool:
            playRound(player, game_num, turn, True)

        #If we are in a recursive call, we are now done. No need to adjust fitness. Reset rollbool.
        if recursive_call:
            rollbool = False
            return

        #Make sure we can see the amount of gold we have
        while g.checkMoney(g.sliceMoney()) == None:
            print("Couldn't see money! Waiting...")
            time.sleep(1)

        #Since we can see a gold value, set the variable
        gold = g.checkMoney(g.sliceMoney())

        #Print the amount of gold we have
        print("Gold: " + str(gold))

        #If we are not in a recursive call, we can adjust the fitness and end the turn
        if not recursive_call:
            player.fitness -= gold
            #Print the loss of fitness due to gold
            print("Uh oh, lost " + str(gold) + " fitness due to unspent gold!")
        
        #End the turn
        endTurn()
        print("Ended turn!")

        rollbool = False

        return turn + 1

'''Function which takes in a player object, and plays through a full game'''
def playGame(player, game_num):

    #Global variables
    global playing

    #Initialize a variable to keep track of the turn number
    turn = 1

    #If we are not playing a game, start.
    if not playing:
        playing = True
    
    #Print the game number
    print('Playing game number ' + str(game_num))

    #Play the game until a terminal loss or win is detected, adjusting the fitness each round.
    while playing:

        #Play round and update turn
        turn = playRound(player, game_num, turn, False)

        '''At this point, the player has just clicked the "End Turn" button, so
        we need to wait for the battle to conclude and check the outcome.'''

        #While we have no outcome or no loss data, wait
        while g.checkOutcome(g.sliceOutcome()) == None:
            while g.checkLoss() == None:
                print("Checking Loss...")
                time.sleep(3)
            print("Waiting patiently for battle to conclude...")
            time.sleep(2)
            if g.checkLoss():
                break
        
        #Since have outcome and loss data, check for a terminal loss
        if g.checkLoss() == True:
            print("Terminal loss detected!")
            playing = False
            player.fitness -= 15
            return game_num + 1

        #If we haven't terminally lost, we can check the outcome
        if g.checkLoss() == False:
            #If we won, adjust fitness accordingly
            if g.checkOutcome(g.sliceOutcome()) == 1:
                print("WooHoo! Won a round!")
                player.fitness += 10
                return game_num

            #If we lost, adjust fitness accordingly
            if g.checkOutcome(g.sliceOutcome()) == 0:
                print("Oh no! Lost a round!")
                player.fitness -= 10
                return game_num

            #If we drew, adjust fitness accordingly
            if g.checkOutcome(g.sliceOutcome()) == 2:
                print("Well, a Draw is a Draw!")
                player.fitness += 1
                return game_num
            
            #Wait one last time to make sure it's a real win
            else:
                print("FINAL EMERGENCY WAIT SEQUENCE")
                time.sleep(6.6)
            
            #If we have a real win, adjust fitness accordingly
            if g.checkLoss() == False:
                print("WooHoo! Won a game!")
                player.fitness += 100
                playing = False
                return game_num + 1