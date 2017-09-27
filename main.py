#!/usr/bin/python3
import sys, pygame
import xml.etree.ElementTree as xmlparser
pygame.init()

white = 255, 255, 255
red = 255, 0, 0
yellow = 255, 255, 0
yellow = 0, 255, 0

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("assets/ball.png")
ballrect = ball.get_rect()

font = pygame.font.Font("assets/Cantarell-Regular.ttf", 32)
text = font.render("The Ball", 2, white)

sound = pygame.mixer.Sound("assets/146726__fins__jumping.wav")

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
		sound.play()
		
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		sound.play()

	screen.fill(black)
	screen.blit(ball, ballrect)
	screen.blit(text, (4, 4))
	pygame.display.flip()