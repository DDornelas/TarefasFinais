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
dt=0.002

p1=Pacote(6371, 0)

tmax=1
t=np.arange(0, tmax, dt)
px=np.zeros(t.size)
py=np.zeros(t.size)

for i in range(t.size):
	p1.move()
	py[i]=p1.y
	
fig = plt.figure()
plt.title('Viagem ao Centro da Terra', fontsize=14)

plt.xticks(np.linspace(-0.06, 0.06, 0.02,endpoint=True), ['', ''])
plt.yticks(np.linspace(-8000, 8000, 2000,endpoint=True), ['', ''])
XxY=fig.add_subplot(111, xlim=(-0.06, 0.06), ylim=(min(py)-300, max(py)+300))
plt.xlabel('X(km)')
plt.ylabel('Y(km)')
plt.grid()
line1, = XxY.plot([], [], 'r.')

def init():
	line1.set_data([],[])
	return line1,
	
def animate(i):
	x=px[i]
	y=py[i]
	line1.set_data(x, y)
	return line1,
		
anim=animation.FuncAnimation(fig, animate, init_func=init, frames = 1000,
interval=0, blit=True)

anim.save('Teste3.mp4', fps=30)

plt.show()
