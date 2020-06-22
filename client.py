import pygame
import socket
from colors import *

pygame.init()

windowWidth = 500
windowHeight = 500

window1 = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("EJTW")
window1.fill((255,255,255))
pygame.display.update()

class Network():
	def __init__(self, ip: str = "localhost"):
		self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverIP:str = "127.0.0.1"
		self.port:int = 55774
		self.address = (self.serverIP, self.port)
		self.id = self.connect()
		print(self.id)
	
	def connect(self):
		try:
			self.clientSocket.connect(self.address)
			return self.clientSocket.recv(2048).decode()
		except Exception as err:
			print("err: ", str(err))

class Player():
	def __init__(self, x, y, size, speed, color):
		self.x = int(x)
		self.y = int(y)
		self.size = int(size)
		self.color = color
		self.speed = int(speed)
		self.rect = (x, y, size, size)
	
	def draw(self, window):
		pygame.draw.rect(window, self.color, self.rect)
	
	def move(self, wWidth, wHeight):
		keys = pygame.key.get_pressed()
		if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (self.x + self.speed < wWidth - self.size):
			self.x += self.speed
		elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (self.x - self.speed > 0):
			self.x -= self.speed
		if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (self.y + self.speed < wHeight - self.size):
			self.y += self.speed
		elif (keys[pygame.K_UP] or keys[pygame.K_w]) and (self.y - self.speed > 0):
			self.y -= self.speed
		self.rect = (self.x, self.y, self.size, self.size)

def updateWindow(window):
	window.fill((255,255,255))
	
	playerSolo.draw(window)
	
	pygame.display.update()

playerSolo = Player(windowWidth // 2 - 25 // 2, windowHeight // 2 - 25 // 2, 25, 5, clBlue)

def main():
	run = True
	while run:		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		playerSolo.move(windowWidth, windowHeight)
		
		updateWindow(window1)
		pygame.time.delay(17)
	
main()
pygame.quit()