import matplotlib.pyplot as plt
import math
import numpy as np

class Bola:	
	def __init__(self, vx, w, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.vx = vx
		self.vy = 0
		self.vz = 1
		self.w = w
				
	def accel(self, vt):
		ax=-vt*v*Bm
		az=-vt*self.w*Sm
		return ax, -g, az
		
	def move(self,):
		ax, ay, az = self.accel(math.sqrt((self.vx**2) + self.vy**2))
		self.x = self.x + self.vx*dt + 0.5*ax*dt**2
		self.vx = self.vx + 0.5*ax*dt
		self.y = self.y + self.vy*dt + 0.5*ay*dt**2
		self.vy = self.vy + 0.5*ay*dt
		self.z = self.z + self.vz*dt + 0.5*az*dt**2
		self.vz = self.vz + 0.5*az*dt
		
g=9.8
Sm=4.1*10**(-4)
Bm=4*10**(-5)
dt=0.01
v=31.29
px=[0]
py=[1]
pz=[0]
velx=[31.29]
vely=[0]
velz=[1]

b1=Bola(31.29, 30, 0, 1, 0)

while(b1.y>=0):
	b1.move()
	px.append(b1.x)
	py.append(b1.y)
	pz.append(b1.z)
	velx.append(b1.vx)
	vely.append(b1.vy)
	velz.append(b1.vz)

plt.figure(figsize=(6,5), dpi=96)

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'$X_{(t)}$(m)')
plt.ylabel(r'$Y_{(t)}$ e $Z_{(t)}$(m)')

plt.title(r'Lan\c{c}amento de Proj\'{e}til', fontsize=12)
plt.grid()
plt.plot(px, py, 'r-', label="XxZ")
plt.plot(px, pz, 'b-', label="XxY")
plt.legend(loc='upper right')
plt.savefig("Teste2.pdf", dpi=96)
plt.show()
