import pygame as py
import pygame.mouse
from pygame.locals import *
from Game import Game,display1
py.init()
g=Game()
class player:
	moves=0
	symbol=0
	name=''
	wins=0
	diagWins=[[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]
	horizWins=[[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)]]
	vertWins=[[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]]
	winList=[diagWins,horizWins,vertWins]
	# noinspection DuplicatedCode
	winDict={(0,0):[[(0,0),(1,1),(2,2)], [(0,0),(1,0),(2,0)],[(0,0),(0,1),(0,2)]],(0,1):[[(0,1),(1,1),(2,1)], [(0,0),(0,1),(0,2)]], (0,2):[[(2,0),(1,1),(0,2)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (0, 1), (0, 2)]], (1, 0): [[(0, 0), (1, 0), (2, 0)], [(1, 0), (1, 1), (1, 2)]], (1, 1): [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)], [(0, 1), (1, 1), (2, 1)], [(1, 0), (1, 1), (1, 2)]], (1, 2): [[(0, 2), (1, 2), (2, 2)], [(1, 0), (1, 1), (1, 2)]], (2, 0): [[(2, 0), (1, 1), (0, 2)], [(0, 0), (1, 0), (2, 0)], [(2, 0), (2, 1), (2, 2)]], (2, 1): [[(0, 1), (1, 1), (2, 1)], [(2, 0), (2, 1), (2, 2)]], (2, 2): [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 2), (2, 2)], [(2, 0), (2, 1), (2, 2)]]}
	winDiagDict={tuple(diagWins[0]):[(0,0),(300,300)],tuple(diagWins[1]):[(0,300),(300,0)]}


	def __init__(self,name,colour,game=g,screen_object=g.screen,draw_object=g.draw):
		self.name=name
		self.board=screen_object
		self.pen=draw_object
		self.color=colour
		self.Game=game


	def sync(self,x,y):
		self.moves+=1
		print("y,x:",y//100,x//100)
		self.Game.matrix[y//100][x//100]=self.symbol
		print(self.name + " moves:", self.moves)
		if self.moves >= 3:return self.checkWin(x//100,y//100)


	def checkWin(self,x,y):
		#print((x,y))
		# noinspection DuplicatedCode
		a=[(-1,-1),(-1,-1),(-1,-1)]
		checkList=self.winDict[(x,y)]
		result=self.checkThroughList(x,y,checkList)
		print(result,self.moves)
		if result!=a:self.drawWin(result);self.wins+=1;self.Game.state=1
		return result


	def checkThroughList(self, x, y, array):
		for j in array:
			#print(j,(x,y)in j)
			if (x,y) not in j:continue
			if all(self.Game.matrix[b][a]==self.symbol for (a,b) in j):
				return j
		return [(-1,-1),(-1,-1),(-1,-1)]

	def drawWin(self,coordinates):
		sp=coordinates[0]
		def new_cord(x):return x*100
		fx,fy=self.normaliseCoods(new_cord(sp[0]),new_cord(sp[1]))
		if coordinates in self.vertWins:
			self.pen.line(self.board,"red",(fx+50,fy),(fx+50,fy+300),width=5)
		elif coordinates in self.horizWins:
			self.pen.line(self.board,"red",(fx,fy+50),(fx+300,fy+50),width=5)
		elif coordinates in self.diagWins:
			cod=self.winDiagDict[tuple(coordinates)]
			cod[0]=self.normaliseCoods(*cod[0])
			cod[1]=self.normaliseCoods(*cod[1])
			self.pen.line(self.board,"red",cod[0],cod[1],width=5)
		py.display.update()
		py.time.wait(1000)

	def normaliseCoods(self,x,y):
		return (x+display1.board_startx,y+display1.board_starty)



class playerX(player):
	symbol=-1

	def draw_shape(self,x,y):
		dx,dy=self.normaliseCoods(x,y)
		self.pen.line(self.board,self.color,(dx+15,dy+15),(dx+85,dy+85),5)
		self.pen.line(self.board,self.color,(dx+85,dy+15),(dx+15,dy+85),5)
		py.display.update()
		return self.sync(x,y)


class playerO(player):
	symbol=1

	def draw_shape(self,x,y):
		dx,dy = self.normaliseCoods(x,y)
		self.pen.circle(self.board,self.color,(dx+50,dy+50),40,width=5)
		py.display.update()
		self.sync(x,y)
