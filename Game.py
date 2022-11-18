import pygame as py
import pygame.mouse
from pygame.locals import *
from Screen import Screen
py.init()


display1=Screen()
display1.drawGameStart()


class Game:
	matrix=[[0,0,0],[0,0,0],[0,0,0]]
	state=0
	winner=0
	turn=0
	display=display1.display
	screen=display1.screen
	draw=display1.draw
	font=display1.font
	players=[]
	l=[0,100,200,300]
	one_player_button=display1.one_player_button
	two_player_button=display1.two_player_button
	exit_button=display1.end_button
	continue_button=display1.con_2p_button
	menu_button=display1.mainMenu
	screenState=0


#	def mouseInbounds(self,x,y):
#		if self.board_startx<=x<=self.board_startx+300 and self.board_starty<=y<=self.board_starty+300:
#


	def init_2p_game(self):
		self.winner=0
		self.state=0
		self.matrix=[[0,0,0],[0,0,0],[0,0,0]]
		self.turn=0
		self.menu_button.state=0
		self.continue_button.state=0
		display1.initBoard(self.players)


	def init_main_menu(self):
		self.screenState=0
		display1.drawGameStart()



	def calc(self,x, y):
		for i in self.l:
			if max(x, i) == i: x = i;break
		for i in self.l:
			if max(y, i) == i: y = i;break
		return [x-100,y-100]


#game start button code
	def nextState(self):
		for event in py.event.get():
			if event.type==QUIT:py.quit()
			pos = py.mouse.get_pos()
			if event.type == MOUSEBUTTONDOWN:
				if self.two_player_button.isOver(pos):
					self.init_2p_game()
					self.screenState+=1
					print("True")
				elif self.exit_button.isOver(pos):
					py.quit()
					print("Exited")
					break
#2p main game


	def gameMainLoop(self):
		for event in py.event.get():
#			self.drawMousePos(*py.mouse.get_pos())
			if event.type==QUIT:py.quit()
			if event.type==MOUSEBUTTONDOWN:
				mouse_pos=py.mouse.get_pos()
				if self.continue_button.isOver(mouse_pos):
					self.init_2p_game();break
				if self.menu_button.isOver(mouse_pos):
					#self.continue_button.state=0
					self.init_main_menu();break
				#put button conditions above
				if (display1.board_startx<mouse_pos[0]<display1.board_startx+300) and (display1.board_starty<mouse_pos[1]<display1.board_starty+300) and self.state==0:
					X,Y=mouse_pos
					X=X-display1.board_startx
					Y=Y-display1.board_starty
					X,Y=self.calc(X,Y)
					mx=X//100;my=Y//100
					print(mx,my)
					if self.matrix[my][mx]!=0:continue
					player=self.players[self.turn%2]
					player.draw_shape(X,Y)
					print("board:")
					for i in self.matrix: print(*i)
					self.turn+=1
					print("turn:",self.turn)
					print("game state:",self.state)
					print("Menu Button state:",self.menu_button.state)
					print("Continue Button State:",self.continue_button.state)
					if self.state==1:
						display1.GameWinMessage(player)
						print("winner is:",player.name);continue
					if self.turn==9 and self.state==0:
						print("Game is tied");continue
