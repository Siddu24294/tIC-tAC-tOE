import pygame.mouse
from pygame.locals import *
import pygame as pyg
from Screen import display1
pyg.init()
#g=Game()
class player:
	moves=0
	symbols=[-1,1]
	symbol=0
	name=''
	wins=0

	is_current_player=False

	diagWins=(((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2)))
	# noinspection DuplicatedCode
	horizWins=(((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)))
	allMoves=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
	# noinspection DuplicatedCode
	vertWins=(((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)))
	winList=[diagWins,horizWins,vertWins]
	display=display1.display
	screen=display1.screen
	draw=display1.draw
	font=display1.font

	turn_holder_coords=(55,196)
	turn_surface=pyg.Surface((100,30))
	score_holder_coords=()
	# noinspection DuplicatedCode

	winDict={
		(0,0):(((0,0),(1,1),(2,2)),((0,0),(1,0),(2,0)),((0,0),(0,1),(0,2))),
		(0,1):(((0,1),(1,1),(2,1)),((0,0),(0,1),(0,2))),
		(0,2):(((2,0),(1,1),(0,2)),((0,2),(1,2),(2,2)),((0,0),(0,1),(0,2))),
		(1,0):(((0,0),(1,0),(2,0)),((1,0),(1,1),(1,2))),
		(1,1):(((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2)),((0,1),(1,1),(2,1)),((1,0),(1,1),(1,2))),
		(1,2):(((0,2),(1,2),(2,2)),((1,0),(1,1),(1,2))),
		(2,0):(((2,0),(1,1),(0,2)),((0,0),(1,0),(2,0)),((2,0),(2,1),(2,2))),
		(2,1):(((0,1),(1,1),(2,1)),((2,0),(2,1),(2,2))),
		(2,2):(((0,0),(1,1),(2,2)),((0,2),(1,2),(2,2)),((2,0),(2,1),(2,2)))
	}
	winDiagDict={tuple(diagWins[0]):((0,0),(300,300)),tuple(diagWins[1]):((0,300),(300,0))}


	def __init__(self,name,colour,game,score_coords:tuple,screen_object=screen,draw_object=draw,p2_parameter=0):
		self.name=name
		self.board=screen_object
		self.pen=draw_object
		self.color=colour
		self.Game=game
		self.score_holder_coords=score_coords
		self.score_surface=pyg.Surface((70,30))
		self.symbol=self.symbols[(self.Game.seriesGame+p2_parameter)%2]


	def __str__(self):
		return f'name:{self.name}' \
		       f'\nwins:{self.wins}' \
		       f'\nmoves made:{self.moves}' \
		       f'\nCurrent move:{self.is_current_player}'


	def scoreUpdater(self):
		self.score_surface.fill((0,0,0))
		score=self.font.render(self.name+":"+str(self.wins),True,self.color)
		self.score_surface.blit(score,(0,0))
		self.screen.blit(self.score_surface,self.score_holder_coords)
		self.display.update()

	def turnDisplayer(self):
		self.turn_surface.fill((0,0,0))
		turn=self.font.render("Turn:"+self.name,True,self.color)
		self.turn_surface.blit(turn,(0,0))
		self.screen.blit(self.turn_surface,(196,55))
		self.display.update()


	def checkThroughList(self, x, y, array):
		for j in array:
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
			cod=[self.winDiagDict[tuple(coordinates)]][0]
			print("elf:",*self.winDiagDict[tuple(coordinates)])
			print("diagnol coordinates are:",*cod)
			cod=(self.normaliseCoods(*cod[0]),self.normaliseCoods(*cod[1]))
			self.pen.line(self.board,"red",cod[0],cod[1],width=5)
			print("diagnol coordinates are:",*cod)
		self.scoreUpdater()
		pyg.display.update()
		pyg.time.wait(1000)


	def normaliseCoods(self,x,y):
		return (x+display1.board_startx,y+display1.board_starty)


	def draw_shape(self,x,y):
		dx=x+display1.board_startx
		dy=y+display1.board_starty

		x=x//100
		y=y//100

		if self.symbol==-1:
			self.pen.line(self.board,self.color,(dx+15,dy+15),(dx+85,dy+85),5)
			self.pen.line(self.board,self.color,(dx+85,dy+15),(dx+15,dy+85),5)

		elif self.symbol==1:
			self.pen.circle(self.board,self.color,(dx+50,dy+50),40,width=5)
		pyg.display.update()

		self.Game.matrix[y][x]=self.symbol
		self.moves+=1
		print(self.name+" moves:",self.moves)
		if self.moves>=3:
			a=[(-1,-1),(-1,-1),(-1,-1)]
			checkList=self.winDict[(x,y)]
			result=self.checkThroughList(x,y,checkList)
			print("winning Combination:",result)
			if result!=a:
				self.wins+=1
				self.drawWin(result)
				self.Game.state=1


#	def sync(self,x,y):
#		self.moves+=1
#		print("(y,x):(",y//100,x//100,")")
#		self.Game.matrix[y//100][x//100]=self.symbol
#		print(self.name + " moves:", self.moves)
#		if self.moves >= 3:return self.checkWin(x//100,y//100)


#	def checkWin(self,x,y):
#		#print((x,y))
#		# noinspection DuplicatedCode
#		a=[(-1,-1),(-1,-1),(-1,-1)]
#		checkList=self.winDict[(x,y)]
#		result=self.checkThroughList(x,y,checkList)
#		print("winning Combination:",result)
#		if result!=a:self.wins+=1;self.drawWin(result);self.Game.state=1
#		return result
