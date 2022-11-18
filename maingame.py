import pygame as py
import pygame.mouse
from pygame.locals import *
from Player import player,playerO,playerX,g
from Game import Game

py.init()
player_list=[playerX('X',"green"),playerO('O',"red")]
g.players=player_list
print(Game.players)
screenStates=[g.nextState,g.gameMainLoop]
while True:
	screenStates[g.screenState]()
