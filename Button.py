import pygame as pyg
from pygame.locals import *

pyg.init()


class Button:

	def __init__(self,text:"enter text", fontObject:"pyg.font.sysfont object", displayObject:"pyg.display object", screenObject:"pyg.display.set_mode object",drawObject:"pyg.draw object"):
		self.text = text
		self.font = fontObject
		self.display = displayObject
		self.screen = screenObject
		self.draw=drawObject
		self.state=0  # used to determine if the button has yet been drawn

	def drawButton(self:"x,y,color,bgcolor", x, y,color,bgcolor):
		textSize = self.font.size(self.text)
		self.x=x
		self.y=y
		self.ex=x+textSize[0]
		self.ey=y+textSize[1]
		self.state=1
#		print("textsize:",textSize)
		but=self.font.render(self.text,True,color,bgcolor)
		self.screen.blit(but,(x,y))
		self.display.update()

	def isOver(self,pos):
		if self.state==1:
			if self.x<pos[0]<self.ex and self.y<pos[1]<self.ey:self.state=0;return True
		return False
