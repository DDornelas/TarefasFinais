#!/usr/bin/env python
import pygame
import sys
from pygame.locals import*
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation
import math

class Pacote:	
	def __init__(self, y, vy):
		self.x = 0
		self.y = y
		self.vy = vy
				
	def accel(self, r):
		a = G*M*r/(R**3)
		return a
		
	def move(self,):
		if(self.y > 0):
			a = self.accel(self.y)
			self.y = self.y + self.vy*dt - 0.5*a*dt**2
			self.vy = self.vy - 0.5*a*dt
		else:
			a = self.accel(-self.y)
			self.y = self.y + self.vy*dt + 0.5*a*dt**2
			self.vy = self.vy + 0.5*a*dt
		
G=6.67*10**(-11)
M=5.9*10**24
R=6371
dt=0.0001

p1=Pacote(-6371, 0)

pygame.init()
screen = pygame.display.set_mode((600,600))

space = pygame.image.load("milkyway.png").convert()
planet = pygame.image.load("Jupter.png").convert_alpha()
ball = pygame.image.load("Esferas.png").convert_alpha()
ball = pygame.transform.scale(ball,(30, 20))
planetw,planeth=planet.get_size()

while True:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	
	screen.blit(space, (0,0))
	screen.blit(planet, (300-planetw/2,300-planeth/2))
	p1.move()
	screen.blit(ball, (287, ((p1.y/6371)*150)+290))
	pygame.display.set_caption('Viagem ao Centro da Terra')
			
	pygame.display.update()


