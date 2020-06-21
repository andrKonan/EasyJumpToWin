import pygame
import time
from colors import *

pygame.init()
pygame.font.init()

windowWidth = 500
windowHeight = 500

window = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("EJTW")
window.fill((255,255,255))
pygame.display.update()

def getMilliseconds() -> int:
	return int(round(time.time() * 1000))

def displayText(text: str, x: int, y: int, color = (0, 0, 0), center: bool = True, size: int = 64):
	font = pygame.font.Font("FantasqueSansMono-Regular.ttf", 16)
	txt = font.render(text, True, color)
	if center == True:
		x -= (txt.get_width() // 2)
		y -= (txt.get_height() // 2)
	window.blit(txt, (int(x), int(y)))

def displayButton(text: str = "", textColor = (0, 0, 0), x: int = 0, y: int = 0, width: int = 20, height: int = 10, buttonColor = (0, 0, 0), borderColor = (255, 255, 255), borderSize: int = 0, center: bool = True):
	if center == True:
		x -= (width / 2)
	pygame.draw.rect(window, buttonColor, (int(x), int(y), int(width), int(height)))

programmState = "menu"
menuState = "main"
menuTimer = getMilliseconds()
leftClick = 0

run = True
while run:
	#exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
	if leftClick == 0 and pygame.mouse.get_pressed()[0] == 1:
		leftClick = 1
	elif leftClick == 1 and pygame.mouse.get_pressed()[0] == 1:
		leftClick = 2
	elif leftClick == 2 and pygame.mouse.get_pressed()[0] == 0:
		leftClick = 0
	
	if programmState == "menu" and leftClick == 1:
		mouse = pygame.mouse.get_pos()
		if menuState == "main":
			if (windowWidth / 4 - 125 / 2) < mouse[0] < (windowWidth / 4 + 125 / 2) and ((windowHeight / 4) * 3) < mouse[1] < ((windowHeight / 4) * 3 + 35) and leftClick == 1:
				menuState = "play"
		elif menuState == "play":
			if (windowWidth / 2 - 165 / 2) < mouse[0] < (windowWidth / 2 + 165 / 2) and ((windowHeight / 4) * 3) < mouse[1] < ((windowHeight / 4) * 3 + 40) and leftClick == 1:
				menuState = "main"
	
	if programmState == "menu":
		mouse = pygame.mouse.get_pos()
		if menuState == "main":
			window.fill((255,255,255))
			displayText("EasyJumpToWin", (windowWidth / 2), 32, clBlack, True, 32)
			
			displayButton(x = (windowWidth / 4), y = (windowHeight / 4) * 3, width = 125, height = 35, buttonColor = clBlue)
			displayText("Play", (windowWidth / 4), (windowHeight / 4) * 3 + 18, color = clWhite, size = 30)
			
			displayButton(x = ((windowWidth / 4) * 3), y = ((windowHeight / 4) * 3), width = 225, height = 35, buttonColor = clBlue)
			displayText("Another button", (windowWidth / 4) * 3, (windowHeight / 4) * 3 + 18, color = clWhite, size = 24)
			
		elif menuState == "play":
			window.fill((255,255,255))
			
			displayButton(x = (windowWidth / 2), y = (windowHeight / 4) * 1, width = 165, height = 40, buttonColor = clBlue)
			displayText("Host", (windowWidth / 2), (windowHeight / 4) * 1 + 20, color = clWhite, size = 32)
			
			displayButton(x = (windowWidth / 2), y = (windowHeight / 4) * 2, width = 165, height = 40, buttonColor = clBlue)
			displayText("Connect", (windowWidth / 2), (windowHeight / 4) * 2 + 20, color = clWhite, size = 32)
			
			displayButton(x = (windowWidth / 2), y = (windowHeight / 4) * 3, width = 165, height = 40, buttonColor = clBlue)
			displayText("Menu", (windowWidth / 2), (windowHeight / 4) * 3 + 20, color = clWhite, size = 32)
			
	pygame.time.delay(16)
	pygame.display.update()
			
	
pygame.quit()