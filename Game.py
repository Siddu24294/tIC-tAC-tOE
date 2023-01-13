import time

import pygame.mouse
import pygame as pyg
from pygame.locals import *
from Screen import display1
from Player import player
from Computer import Computer
pyg.init()


display1.drawGameStart()

class Game:
	matrix=[[0,0,0],[0,0,0],[0,0,0]]
	#game variables
	state=0
	winner=0
	turn=0
	players=[]
	l=[0,100,200,300]
	screenState=0
	seriesGame=0
	is_game_over=False

	computer_player=0
	#turn wise variable
	current_player=0
	next_player=0
	#default variables
	display=display1.display
	screen=display1.screen
	draw=display1.draw
	font=display1.font
	#buttons
	one_player_button=display1.one_player_button
	two_player_button=display1.two_player_button
	exit_button=display1.end_button
	continue_button=display1.con_2p_button
	menu_button=display1.mainMenu



#	def mouseInbounds(self,x,y):
#		if self.board_startx<=x<=self.board_startx+300 and self.board_starty<=y<=self.board_starty+300:
#


	def init_game_board(self):
		self.winner=0
		self.state=0
		self.matrix=[[0,0,0],[0,0,0],[0,0,0]]
		self.turn=0
		self.menu_button.state=0
		self.continue_button.state=0
		self.players=self.players[::-1]
		display1.initBoard(self.players)
#		print("-----------Insied init 2p-------------")
#		print("+++++++++++++++++++++++++++++++++++++++")
#		print(self.players)
#		print("init 2p executed")

		if type(self.computer_player)==Computer:
			self.computer_player.movesList=list(self.computer_player.allMoves)

		self.current_player=self.players[0]
		self.current_player.is_current_player=True
		self.current_player.scoreUpdater()

		self.next_player=self.players[1]
		self.next_player.is_current_player=False
		self.next_player.scoreUpdater()

		self.is_game_over=False
#		print(self.current_player)
#		print(self.is_game_over)
#		print("+++++++++++++++++++++++++++++++++++++++")
#		print("--------------------------------------")#

		self.s=pyg.Surface((100,100))
		self.s.fill((0,0,0))

		self.current_player.turnDisplayer()


	def init_main_menu(self):
		self.is_game_over=False
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
		for event in pyg.event.get():
			if event.type==QUIT:pyg.quit()
			pos = pyg.mouse.get_pos()
			if event.type == MOUSEBUTTONDOWN:

				if self.one_player_button.isOver(pos):
					self.players=[Computer('O','red',self,(10,400),p2_parameter=1),player('X',"green",self,(10,430))]
					self.computer_player=self.players[0]
					self.init_game_board()
					self.screenState=1
					print("1p game initiated")

				elif self.two_player_button.isOver(pos):
					self.players=[player('X',"green",self,(10,400)),player('O',"red",self,(10,430),p2_parameter=1)]
					self.init_game_board()
					self.screenState=1
					print("2p game initiated")

				elif self.exit_button.isOver(pos):
					pyg.quit()
					print("Exited")
					break


	def debugger(self):
		print("*************----------*************\nboard:")
		print('________________\nplayer 1:',self.players[0],'\n_______________')
		print('________________\nplayer 2:',self.players[1],'\n_______________')
		for i in self.matrix: print(*i)
		print(f'''
		\nturn:{self.turn}
game state:{self.state}
Menu Button state:{self.menu_button.state}
Continue Button State:{self.continue_button.state}
Game series state:{self.seriesGame}
''')
		print("*************----------*************")
#2p main game


	def isGameOver(self):
		if self.state==1:

			display1.GameWinMessage(self.current_player)
			print("winner is:",self.current_player.name)

			self.is_game_over=True
			self.current_player.is_current_player=False
			self.next_player.is_current_player=False

			print(self.matrix)
			return True
		elif self.turn>=9 and self.state==0:

			display1.GameDrawMessage()

			self.is_game_over=True
			self.current_player.is_current_player=False
			self.next_player.is_current_player=False

			print("Game is tied")
			return True


	def optimisedCode(self):
		while self.current_player.is_current_player:

			if type(self.current_player)==Computer:
				self.current_player.turnDisplayer()

				print(self.current_player)
				cy,cx=self.current_player.turnMaker()
				self.current_player.draw_shape(cx*100,cy*100)
				print("computer genertaed cooerdintes are:",cx,cy)

				self.turn+=1
				self.debugger()

				#check condition
				if self.isGameOver():break

				self.current_player.is_current_player=False
				self.next_player.is_current_player=True
				self.current_player,self.next_player=self.next_player,self.current_player
				self.current_player.turnDisplayer()

			else:
				for event in pyg.event.get():
					self.s.fill((0,0,0))
					xag,yag=pyg.mouse.get_pos()
					text=display1.font.render(str(xag)+","+str(yag),True,'white')
					self.s.blit(text,(0,0))
					display1.screen.blit(self.s,(400,570))
					display1.display.update()

					if event.type==QUIT: pyg.quit()

					if event.type==MOUSEBUTTONDOWN:
						mouse_pos=pyg.mouse.get_pos()
						#rest of code from above
						if (display1.board_startx<mouse_pos[0]<display1.board_startx+300) and (
								display1.board_starty<mouse_pos[1]<display1.board_starty+300) and self.state==0:

							X,Y=mouse_pos
							X=X-display1.board_startx
							Y=Y-display1.board_starty
							X,Y=self.calc(X,Y)

							mx=X//100
							my=Y//100

							print("starting mouse cordinates are:",mx,my)

							if self.matrix[my][mx]!=0: continue
							self.current_player.draw_shape(X,Y)
							self.turn+=1
							self.debugger()

							#check condition
							if self.isGameOver():break

							self.current_player.is_current_player=False
							self.next_player.is_current_player=True
							self.current_player,self.next_player=self.next_player,self.current_player
							self.current_player.turnDisplayer()

		while self.is_game_over:
			for event in pyg.event.get():
				mouse_pos1=pyg.mouse.get_pos()
				print(mouse_pos1)
				if event.type==QUIT:pyg.quit()

				elif event.type==MOUSEBUTTONDOWN:
					print(self.current_player.is_current_player)
					print(self.is_game_over)
					mouse_pos=pyg.mouse.get_pos()

					if self.continue_button.isOver(mouse_pos):
						self.seriesGame+=1
						self.init_game_board()
						break

					if self.menu_button.isOver(mouse_pos):
						self.is_game_over=False
						self.init_main_menu()
						break



g=Game()