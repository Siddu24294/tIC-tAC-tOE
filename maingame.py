import pygame as pyg
import pygame.mouse
from pygame.locals import *
#from Player import player
from Game import g

pyg.init()
#player_list=[playerX('X',"green"),playerO('O',"red")]
screenStates=[g.nextState,g.optimisedCode]
while True:
	screenStates[g.screenState]()
