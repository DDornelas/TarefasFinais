import matplotlib.pyplot as plt
import math
import numpy as np
import pygame
import sys
from pygame.locals import*
from matplotlib import animation as animation

class MassaMola:	
	def __init__(self, massa, theta, mi, d, k, v):
		self.m = massa
		self.theta = theta
		self.x = d*math.cos(theta)
		self.y = d*math.sin(theta)
		self.vx = v*math.cos(theta)
		self.vy = v*math.sin(theta)
		self.mi = mi
		self.k = k
		self.e = 0.5*massa*(v**2) + massa*g*d
		
	def accel1(self):
		a=-self.m*g*math.cos(self.theta)*(1-self.mi)
		return a*math.cos(self.theta)
		
	def accel2(self, x):
		a=-self.m*g*math.cos(self.theta)*(1-self.mi)+self.k*x/self.m
		return a*math.cos(self.theta)
		
	def move1(self,):
		a=self.accel1()
		self.x = self.x + self.vx*dt + 0.5*a*dt**2
		self.vx = self.vx + 0.5*a*dt
		self.y = self.y + self.vy*dt + 0.5*a*dt**2
		self.vy = self.vy + 0.5*a*dt
		self.e = 0.5*self.m*((math.sqrt((self.vx**2) + 
		(self.vy**2)))**2) + self.m*g*math.sqrt((self.x**2) + 
		(self.y**2))
		
	def move2(self,):
		a=self.accel2(1-math.sqrt((self.x**2)+(self.y**2)))
		self.x = self.x + self.vx*dt + 0.5*a*dt**2
		self.vx = self.vx + 0.5*a*dt
		self.y = self.y + self.vy*dt + 0.5*a*dt**2
		self.vy = self.vy + 0.5*a*dt
		self.e = 0.5*self.m*((math.sqrt((self.vx**2) + 
		(self.vy**2)))**2) + self.m*g*math.sqrt((self.x**2) + 
		(self.y**2)) + 0.5*self.m*(1 - math.sqrt((self.x**2) + 
		(self.y**2)))

def wrap_angle(angle):
	return angle%360

g=9.8
dt=0.01
px=[3*math.cos(np.pi/4)]
py=[3*math.cos(np.pi/4)]
velx=[0]
vely=[0]
energy=[6*g*3]

b1=MassaMola(6, np.pi/4, 0.5, 3, 800, 0)

while(b1.vx<=0):
	
	if(math.sqrt((b1.x**2)+(b1.y**2))>1):
		b1.move1()
		px.append(b1.x)
		py.append(b1.y)
		velx.append(b1.vx)
		vely.append(b1.vy)
		energy.append(b1.e)
	
	else:
		b1.move2()
		px.append(b1.x)
		py.append(b1.y)
		velx.append(b1.vx)
		vely.append(b1.vy)
		energy.append(b1.e)
		
pygame.init()
screen = pygame.display.set_mode((600,600))

rampa = pygame.image.load("rampa.jpg").convert()
mola = pygame.image.load("mola.jpg").convert_alpha()
bloco = pygame.image.load("ploco.jpg").convert_alpha()
#planet = pygame.transform.scale(planet,(50,50))
molaw,molah=mola.get_size()

#clock = pygame.time.Clock()
while(b1.vx<=0):
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	
	screen.blit(rampa, (0,0))
	if(math.sqrt((b1.x**2)+(b1.y**2))>1):
		screen.blit(mola, (5,10))
		xant, yant = b1.x, b1.yt
		b1.move1()
		angulo = math.atan2(b1.x, b1.y)
		angulo = wrap_angle(-math.degrees(angulo)+90)
		dayplanet = pygame.transform.rotate(planet, angulo)
		screen.blit(dayplanet, (Terra.xt*250+275, Terra.yt*250+275))
	pygame.display.set_caption('O Sol e a Terra')
	
	pygame.display.update()
	#tempo = clock.tick(60)
