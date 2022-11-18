import pygame as py
from pygame.locals import *
from Button import Button
py.init()


class Screen:
	#display Metrics
	disp_width=500
	disp_height=600

	board_startx=100
	board_starty=100

	#colors
	white=(255,255,255)
	black=(0,0,0)
	blue=(0,0,255)
	green=(0,255,0)
	red=(255,0,0)

	#board lines
	horizLine1=[(board_startx+100,board_starty),(board_startx+100,board_starty+300)]
	horizLine2=[(board_startx+200,board_starty),(board_startx+200,board_starty+300)]
	vertLine1=[(board_startx,board_starty+100),(board_startx+300,board_starty+100)]
	vertLine2=[(board_startx,board_starty+200),(board_startx+300,board_starty+200)]

	#pygame module variables
	display = py.display
	screen = display.set_mode(size=(disp_width,disp_height))
	draw = py.draw
	font = py.font.SysFont("Comic Sans MS", 24)
	screenState=0
#	screens=[gameStart,mainGame,gameOver]
	title_color=(255,255,255)
	screen_background=(0,0,0)
	one_player_button=Button("Computer",font,display,screen,draw)
	two_player_button = Button("2 Players",font,display,screen,draw)
	end_button = Button("Exit", font, display, screen, draw)
	con_2p_button=Button("Continue", font, display, screen, draw)
	mainMenu=Button("Main Menu",font,display,screen,draw)


#Section -1


	def drawGameStart(self,font=font,screen=screen,display=display):
		screen.fill(self.screen_background)
		self.blitSurfText("Tic Tac Toe",1)
		self.one_player_button.drawButton(75,200,self.white,self.red)
		self.two_player_button.drawButton(75,300,self.white,self.red)
		self.end_button.drawButton(75,400,self.white,self.red)
		self.display.update()


	def blitSurfText(self,string,center=1,fontColor=title_color,font=font,screen=screen,display=display):
		textSurf=font.render(string,True,fontColor)
		textRect=font.size(string)
		textW,textH=textRect
		surf=py.Surface(textRect)
		surf.blit(textSurf,(0,0))
		x=(self.disp_width-textW)/2
		y=(self.disp_width-textW)/2
		if center!=1:x=center[0],y=center[1]
		screen.blit(surf,(x,y))
		display.update()

# Section -2


	#def initBoard(self,players):
	#	self.drawBoard(players)


	def initBoard(self,players:"list of players",screen=screen):
		self.screen.fill(self.black)
		self.draw.line(screen, self.white, *self.horizLine1, 5)
		self.draw.line(screen, self.white, *self.horizLine2, 5)
		self.draw.line(screen, self.white, *self.vertLine1, 5)
		self.draw.line(screen, self.white, *self.vertLine2, 5)
		self.drawString(players)
		self.display.update()

	def drawString(self,players:"list of players",screen=screen,font=font):
		player0=players[0]
		player1=players[1]
		img = font.render(player0.name + ":"+str(player0.wins), True, player0.color)
		screen.blit(img, (10, 400))
		img1 = font.render(player1.name + ":"+str(player1.wins), True, player1.color)
		screen.blit(img1, (160, 400))
		img = font.render("Mouse X:", True, self.white)
		screen.blit(img, (10, 450))
		img = font.render("Mouse Y:", True, self.white)
		screen.blit(img, (160, 450))



	def drawMousePos(self,x,y,screen=screen,font=font):
		screen.fill(self.black)
		imgX=font.render(str(x),True,self.white)
		screen.blit(imgX,(100,450))
		imgY=font.render(str(y),True,self.white)
		screen.blit(imgY,(250,450))


	def GameWinMessage(self,player,screen=screen,font=font):
		img=font.render(player.name+"Wins",True,self.blue)
		screen.blit(img,(100,400))
		self.con_2p_button.drawButton(50, 550, self.red, self.white)
		self.mainMenu.drawButton(250,550,self.red,self.green)
		#py.display.update()

