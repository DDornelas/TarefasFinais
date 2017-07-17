import matplotlib.pyplot as plt
import math
import numpy as np
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
		a=-g*math.cos(self.theta)*(1-self.mi)
		return a*math.cos(self.theta)
		
	def accel2(self, x):
		a=-g*math.cos(self.theta)*(1-self.mi)+self.k*x/self.m
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

g=9.8
dt=0.01
px=[3*math.cos(np.pi/4)]
py=[3*math.cos(np.pi/4)]
velx=[0]
vely=[0]
energy=[6*g*3]
t=1

b1=MassaMola(6, np.pi/4, 0.5, 3, 800, 0)

while(b1.vx<=0):
	
	if(math.sqrt((b1.x**2)+(b1.y**2))>1):
		b1.move1()
		px.append(b1.x)
		py.append(b1.y)
		velx.append(b1.vx)
		vely.append(b1.vy)
		energy.append(b1.e)
		t = t+1
	
	else:
		b1.move2()
		px.append(b1.x)
		py.append(b1.y)
		velx.append(b1.vx)
		vely.append(b1.vy)
		energy.append(b1.e)
		t = t+1
		
print 't=%d' %(t)	
	
fig = plt.figure()
plt.title('Bloco na Rampa Com Mola', fontsize=14)

plt.xticks(np.linspace(0, 2.5, 0.5,endpoint=True), ['', ''])
plt.yticks(np.linspace(0, 2.5, 0.5, endpoint=True))
XxY=fig.add_subplot(111, xlim=(0, 2.5), ylim=(0, 2.5))
plt.xlabel('$X_{(t)}$(m)')
plt.ylabel('$Y_{(t)}$(m)')
plt.grid()
line1, = XxY.plot([], [], 'r.', lw=2)

def init():
	line1.set_data([],[])
	return line1,
	
def animate(i):
	x=px[:i]
	y=py[:i]
	line1.set_data(x, y)
	return line1,
		
anim=animation.FuncAnimation(fig, animate, init_func=init, frames = 320,
interval=0, blit=True)

anim.save('Teste1.mp4', fps=30)

plt.show()
