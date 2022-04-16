TABLE OF CONTENTS
---------------------

* Introduction
* Installation 
* Current Issues
* Maintainers

INTRODUCTION
---------------------

This repository serves as the home to my Super Auto Pets AI. There are two classes, Nnet() and Player(). Each Player plays the game, and has an Nnet attribute that can be thought of as its brain. Each player will play a full game of Super Auto Pets, and its fitness will be calculated. The more fit players will breed, and random mutations will be introduced. 

* Some factors taken into consideration when calculating fitness include: ending a turn with unspent gold, losing rounds, winning rounds, drawing rounds, and winning or losing games. 

INSTALLATION
---------------------

There are no current official releases. If you want to run, tweak, or play with this yourself, feel free, although you will likely need a basic understanding of Python and Machine Learning.

* There might one day be an official release! Keep your eyes peeled. 

CURRENT ISSUES
---------------------

As of 4/16/2022, it is imperfect. I have not yet implemented the ability for it to see or interact with food, which is kind of an integral aspect of the game. Additionally, performance would likely increase given the ability to add more hidden abstract neuron layers. Other todo items include: Adding input neurons to represent the turn, current board layout, remaining health, and gold. Allow the AI to recognize frozen items (currently, it just views it as an empty slot).

MAINTAINERS
---------------------

This repository is currently Eli's Hobby project, although if you want to contribute, feel free!

* saltsperkins@gmail.com
* eli@imperatorsecurity.com