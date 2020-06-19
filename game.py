import pygame

pygame.init()

windowWidth = 500
windowHeight = 500

window = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("JEW")
window.fill((255,255,255))
pygame.display.update()

width = 25
height = 25
x = windowWidth // 2 - width // 2
y = windowHeight // 2 - height // 2
speed = 5

isJump = False
totalJumpCount = 10
jumpCount = 10

nmSpeed = 5
slSpeed = 2

run = True
while run:
	pygame.time.delay(16)
	
	#exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	if ((x + (speed * 2) >= windowWidth - width) or (x - (speed * 2) <= 0) or (y + (speed * 2) >= windowHeight - height) or (y - (speed * 2) <= 0)):
		speed = slSpeed
	else:
		speed = nmSpeed
	
	#moving
	keys = pygame.key.get_pressed()
	if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (x + speed < windowWidth - width):
		x += speed
	if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (x - speed > 0):
		x -= speed
	if not(isJump):
		if (keys[pygame.K_SPACE]) and isJump == False:
			isJump = True
	elif isJump:
		if jumpCount >= -(totalJumpCount):
			if ((y - jumpCount ** 2 >= 0) and (y - jumpCount ** 2 <= windowHeight)):
				if jumpCount >= 0:
					y -= (jumpCount ** 2) // 3
				elif jumpCount < 0:
					y += (jumpCount ** 2) // 3
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = totalJumpCount
		
	window.fill((255,255,255))
	pygame.draw.rect(window, (66, 135, 245), (x, y, width, height))
	pygame.display.update()
	
pygame.quit()