import pygame as py
from pygame.locals import *
from Button import Button
py.init()


display=py.display
screen=display.set_mode((500,500))
font=py.font.SysFont("Comic Sans MS",20)
draw=py.draw
b=Button("test",font,display,screen,draw)
b.drawButton(250,250,(0,0,0),(255,255,255))
while True:
	for event in py.event.get():
		if event.type==QUIT:py.quit()
		pos=py.mouse.get_pos()
		if event.type==MOUSEBUTTONDOWN:
			if b.isOver(pos):print("Trye")
			else:print("Flase")