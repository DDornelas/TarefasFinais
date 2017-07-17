import matplotlib.pyplot as plt
import math
import numpy as np

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
energy=[10*g*3]
ei=10*g*3
tp=[0]
t=0
b1=MassaMola(10, np.pi/4, 0.5, 3, 800, 0)

print b1.e

while(b1.vx<=0):
	
	if(math.sqrt((b1.x**2)+(b1.y**2))>1):
		b1.move1()
		px.append(b1.x)
		py.append(b1.y)
		velx.append(b1.vx)
		vely.append(b1.vy)
		energy.append(b1.e)
		#print 'X=%f,\tY=%f\n' %(b1.x, b1.y)
		tp.append(t)
		t=t+dt
	
	else:
		b1.move2()
		px.append(b1.x)
		py.append(b1.y)
		velx.append(b1.vx)
		vely.append(b1.vy)
		energy.append(b1.e)
		#print 'X=%f,\tY=%f\n' %(b1.x, b1.y)
		tp.append(t)
		t=t+dt
	
print b1.e
	
plt.figure(figsize=(6,5), dpi=96)

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'Tempo(s)')
plt.ylabel(r'$E_{(t)}$(J)')

plt.title(r'Bloco na Rampa Com Mola', fontsize=12)
plt.grid()
plt.plot(tp, energy, 'r-')
#plt.legend(loc='upper right')
plt.savefig("EF3.pdf", dpi=96)
plt.show()
