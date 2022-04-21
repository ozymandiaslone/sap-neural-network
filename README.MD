TABLE OF CONTENTS
---------------------

* Introduction
* Installation 
* Current Issues
* Maintainers

INTRODUCTION
---------------------

This repository serves as the home to my Super Auto Pets AI. There are two classes, Nnet() and Player(). interface.py is responsible for interacting with the game. gameviewer.py is responsible for querying the screen to get information about the current gamestate. Each Player plays the game, and has an Nnet attribute that can be thought of as its brain. Each player will play a full game of Super Auto Pets, and its fitness will be calculated. The more fit players will breed, and random mutations will be introduced. 

* Some factors taken into consideration when calculating fitness include: ending a turn with unspent gold, losing rounds, winning rounds, drawing rounds, and winning or losing games. 

INSTALLATION
---------------------

There are no current official releases. If you want to run, tweak, or play with this yourself, feel free, although you will likely need a basic understanding of Python and Machine Learning.

* There might one day be an official release! Keep your eyes peeled. 

CURRENT ISSUES
---------------------
[CURRENT]
completely broken

[OLD]
As of 4/19/2022, it is slightly less imperfect, but still not 100%. It still can't see or interact with food, which opens up lots of possibilites. Additionally, it can't directly swap around the positions of animals which have already been placed on the game board. Neurons for the turn and gold have been fully implemented, and it is in an untested yet believed-to-be-stable state.

[OLD]
As of 4/19/2022, it is slightly less imperfect, but still not 100%. It still can't see or interact with food, which opens up lots of possibilites. Additionally, it can't directly swap around the positions of animals which have already been placed on the game board. I implemented the extra neurons and inputs necessary for the Players' brains to see the animals it currently owns, and their positions.

I still need to implement input neurons for the turn, gold, and remaining health. 

[OLD]
As of 4/16/2022, it is imperfect. I have not yet implemented the ability for it to see or interact with food, which is kind of an integral aspect of the game. Additionally, performance would likely increase given the ability to add more hidden abstract neuron layers. Other todo items include: Adding input neurons to represent the turn, current board layout, remaining health, and gold. Allow the AI to recognize frozen items (currently, it just views it as an empty slot).

MAINTAINERS
---------------------

This repository is currently Eli's Hobby project, although if you want to contribute, feel free!

* saltsperkins@gmail.com
* eli@imperatorsecurity.com