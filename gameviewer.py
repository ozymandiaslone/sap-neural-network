'''-----Imports-----'''
from os import read
import cv2
import numpy as np
import time
import screendata
import pyautogui

'''Functions which returns a screenshot of the game'''
def getGameData():
    image = screendata.grab_raw_screen()
    return image

'''Function which takes in a screenshot and slices it into separate picutres for analysis'''
def sliceImage(turn):

    #Initialize an empty list to store eventual sliced images to return
    images = []
    preslice = getGameData()
    images.append(preslice[590:720, 499:623].copy())
    images.append(preslice[590:720, 633:757].copy())
    images.append(preslice[590:720, 766:890].copy())
    if turn > 4:
        images.append(preslice[590:720, 899:1023].copy())
    if turn > 8:
        images.append(preslice[590:720, 1032:1156].copy())

    return images

'''Function which returns an image for use in money analysis'''
def sliceMoney():
    preslice = getGameData()
    slice = preslice[50:127, 19:156]
    return slice

'''Function which takes in an images and determines the available animals'''
def checkForAnimals(images):
    positions = [None]*3

    #grab images to test against,label them, and put them into a list
    test_images = []
    ant = ("ant",cv2.imread("./images/ANT.jpg"))
    test_images.append(ant)
    cricket = ("cricket",cv2.imread("./images/CRICKET.jpg"))
    test_images.append(cricket)
    beaver = ("beaver",cv2.imread("./images/BEAVER.jpg"))
    test_images.append(beaver)
    pig = ("pig",cv2.imread("./images/PIG.jpg"))
    test_images.append(pig)
    fish = ("fish",cv2.imread("./images/FISH.jpg"))
    test_images.append(fish)
    crab = ("crab",cv2.imread("./images/CRAB.jpg"))
    test_images.append(crab)
    spider = ("spider",cv2.imread("./images/SPIDER.jpg"))
    test_images.append(spider)
    duck = ("duck",cv2.imread("./images/DUCK.jpg"))
    test_images.append(duck)
    mosquito = ("mosquito",cv2.imread("./images/MOSQUITO.jpg"))
    test_images.append(mosquito)
    hedgehog = ("hedgehog",cv2.imread("./images/HEDGEHOG.jpg"))
    test_images.append(hedgehog)
    peacock = ("peacock",cv2.imread("./images/PEACOCK.jpg"))
    test_images.append(peacock)
    flamingo = ("flamingo",cv2.imread("./images/FLAMINGO.jpg"))
    test_images.append(flamingo)
    rat =  ("rat",cv2.imread("./images/RAT.jpg"))
    test_images.append(rat)
    swan = ("swan",cv2.imread("./images/SWAN.jpg"))
    test_images.append(swan)
    shrimp = ("shrimp",cv2.imread("./images/SHRIMP.jpg"))
    test_images.append(shrimp)
    horse = ("horse",cv2.imread("./images/HORSE.jpg"))
    test_images.append(horse)
    otter = ("otter",cv2.imread("./images/OTTER.jpg"))
    test_images.append(otter)
    dodo = ("dodo",cv2.imread("./images/DODO.jpg"))
    test_images.append(dodo)
    turtle = ("turtle",cv2.imread("./images/TURTLE.jpg"))
    test_images.append(turtle)
    snail0 = ("snail0",cv2.imread("./images/SNAIL0.jpg"))
    test_images.append(snail0)
    sheep = ("sheep",cv2.imread("./images/SHEEP.jpg"))
    test_images.append(sheep)
    blowfish = ("blowfish",cv2.imread("./images/BLOWFISH.jpg"))
    test_images.append(blowfish)
    elephant = ("elephant",cv2.imread("./images/ELEPHANT.jpg"))
    test_images.append(elephant)
    giraffe = ("giraffe",cv2.imread("./images/GIRAFFE.jpg"))
    test_images.append(giraffe)
    rabbit = ("rabbit",cv2.imread("./images/RABBIT.jpg"))
    test_images.append(rabbit)
    dog = ("dog",cv2.imread("./images/DOG.jpg"))
    test_images.append(dog)
    kangaroo = ("kangaroo",cv2.imread("./images/KANGAROO.jpg"))
    test_images.append(kangaroo)
    camel = ("camel",cv2.imread("./images/CAMEL.jpg"))
    test_images.append(camel)
    badger = ("badger",cv2.imread("./images/BADGER.jpg"))
    test_images.append(badger)
    ox = ("ox",cv2.imread("./images/OX.jpg"))
    test_images.append(ox)
    parrot = ("parrot",cv2.imread("./images/PARROT.jpg"))
    test_images.append(parrot)
    bison = ("bison",cv2.imread("./images/BISON.jpg"))
    test_images.append(bison)
    rooster = ("rooster",cv2.imread("./images/ROOSTER.jpg"))
    test_images.append(rooster)
    worm = ("worm",cv2.imread("./images/WORM.jpg"))
    test_images.append(worm)
    hippo = ("hippo",cv2.imread("./images/HIPPO.jpg"))
    test_images.append(hippo)
    turkey = ("turkey",cv2.imread("./images/TURKEY.jpg"))
    test_images.append(turkey)
    deer = ("deer",cv2.imread("./images/DEER.jpg"))
    test_images.append(deer)
    whale = ("whale",cv2.imread("./images/WHALE.jpg"))
    test_images.append(whale)
    dolphin = ("dolphin",cv2.imread("./images/DOLPHIN.jpg"))
    test_images.append(dolphin)
    skunk = ("skunk",cv2.imread("./images/SKUNK.jpg"))
    test_images.append(skunk)
    shark = ("shark",cv2.imread("./images/SHARK.jpg"))
    test_images.append(shark)
    snake = ("snake",cv2.imread("./images/SNAKE.jpg"))
    test_images.append(snake)
    mammoth = ("mammoth",cv2.imread("./images/MAMMOTH.jpg"))
    test_images.append(mammoth)
    squirrel  = ("squirrel",cv2.imread("./images/SQUIRREL.jpg"))
    test_images.append(squirrel)
    rhino = ("rhino",cv2.imread("./images/RHINO.jpg"))
    test_images.append(rhino)
    cat = ("cat",cv2.imread("./images/CAT.jpg"))
    test_images.append(cat)
    fly = ("fly",cv2.imread("./images/FLY.jpg"))
    test_images.append(fly)
    dragon = ("dragon",cv2.imread("./images/DRAGON.jpg"))
    test_images.append(dragon)
    gorilla = ("gorilla",cv2.imread("./images/GORILLA.jpg"))
    test_images.append(gorilla)
    crocodile = ("crocodile",cv2.imread("./images/CROCODILE.jpg"))
    test_images.append(crocodile)
    cow = ("cow",cv2.imread("./images/COW.jpg"))
    test_images.append(cow)
    scorpion = ("scorpion",cv2.imread("./images/SCORPION.jpg"))
    test_images.append(scorpion)
    monkey = ("monkey",cv2.imread("./images/MONKEY.jpg"))
    test_images.append(monkey)
    boar = ("boar",cv2.imread("./images/BOAR.jpg"))
    test_images.append(boar)
    seal = ("seal",cv2.imread("./images/SEAL.jpg"))
    test_images.append(seal)
    leopard = ("leopard",cv2.imread("./images/LEOPARD.jpg"))
    test_images.append(leopard)
    tiger = ("tiger",cv2.imread("./images/TIGER.jpg"))
    test_images.append(tiger)
  

    count = 0
    for image in images:
        for test_image in test_images:
            errorL2 = cv2.norm(image, test_image[1], cv2.NORM_L2)
            similarity = errorL2 / (test_image[1].shape[0] * test_image[1].shape[1])
            if similarity < 1:
                positions[count] = test_image[0]
        count += 1
    return positions

#Create a list of tuples containing the image and value, for use in image comparisons
money_test = []
zero = (0, cv2.imread("./images/money0.jpg"))
money_test.append(zero)
one = (1, cv2.imread("./images/money1.jpg"))
money_test.append(one)
two = (2, cv2.imread("./images/money2.jpg"))
money_test.append(two)
three = (3, cv2.imread("./images/money3.jpg"))
money_test.append(three)
four = (4, cv2.imread("./images/money4.jpg"))
money_test.append(four)
five = (5, cv2.imread("./images/money5.jpg"))
money_test.append(five)
six = (6, cv2.imread("./images/money6.jpg"))
money_test.append(six)
seven = (7, cv2.imread("./images/money7.jpg"))
money_test.append(seven)
eight = (8, cv2.imread("./images/money8.jpg"))
money_test.append(eight)
nine = (9, cv2.imread("./images/money9.jpg"))
money_test.append(nine)
ten = (10, cv2.imread("./images/money10.jpg"))
money_test.append(ten)
eleven = (11, cv2.imread("./images/money11.jpg"))
money_test.append(eleven)
twelve = (12, cv2.imread("./images/money12.jpg"))
money_test.append(twelve)
thirteen = (13, cv2.imread("./images/money13.jpg"))
money_test.append(thirteen)
fourteen = (14, cv2.imread("./images/money14.jpg"))
money_test.append(fourteen)

'''Function which takes in an image, and determines the amount of gold currently in inventory'''
def checkMoney(image):
    for i in money_test:
        errorL2 = cv2.norm(image, i[1], cv2.NORM_L2)
        similarity = errorL2 / (i[1].shape[0] * i[1].shape[1])
        if similarity < .1:
            return i[0]

'''Function which returns a correctly cropped image to check round outcome'''
def sliceOutcome():
    preslice = getGameData()
    image = preslice[620:770, 777:840 ]
    return image

'''Function which takes in an image, and compares it against known images to determine the outcome of a round'''
def checkOutcome(image):
    outcome_test = []
    loss = (0, cv2.imread("./images/DEFEAT.jpg"))
    outcome_test.append(loss)
    win = (1, cv2.imread("./images/WIN.jpg"))
    outcome_test.append(win)
    draw = (2, cv2.imread("./images/DRAW.jpg"))
    outcome_test.append(draw)
    outcome = None
    for i in range(0,3):
        errorL2 = cv2.norm(image, outcome_test[i][1], cv2.NORM_L2)
        similarity = errorL2 / (outcome_test[i][1].shape[0] * outcome_test[i][1].shape[1])
        if similarity < .75:
            outcome = money_test[i][0]
    return outcome

'''Function which checks certain pixel color values to check for a terminal loss'''
def checkLoss():
    preslice = getGameData()
    color_data = preslice[950,250]
    #print(color_data[0])
    #print(color_data[1])
    #print(color_data[2])
    if color_data[2] == 0:
        return True
    elif color_data[2] == 244:
        return False
    elif color_data[2] == 255 and color_data[1] == 106:
        return False
    elif color_data[2] == 255:
        return "loop"
    else: return None

#Testing area for when thing inevitably break
#print(checkLoss())