import pygame as pyg
import random as r
from Screen import display1
from Player import player


class Computer(player):
	movesList:list
	def compMoves(self):pass

	def turnMaker(self):
		if self.Game.turn==0:
			self.movesList.remove((1,1))
			return 1,1
		else:
			if self.Game.turn==1:
				if self.Game.matrix[1][1]==0:
					self.movesList.remove((1,1))
					return 1,1
				else:
					self.movesList.remove((0,0))
					return 0,0
			elif self.Game.turn>=2:
				m=r.choice(self.movesList)
				if self.Game.matrix[m[0]][m[1]]!=0:
					self.movesList.remove(m)
					print(m,'removed cause already in matrix')
					return self.turnMaker()
				else:
					self.movesList.remove(m)
					return m
'''		
'''











'''	def abc(self):
		precedence=[4,[0,2,6,8]]

		if 4 empty then put 4
		next move use one corner
		if self.turn >=2 :
			self.winList
		
		
'''