import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import animation as animation

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
dt=0.005
v=31.29
px=[0]
py=[1]
pz=[0]
velx=[31.29]
vely=[0]
velz=[1]
t=0

b1=Bola(31.29, 30, 0, 1, 0)

while(b1.y>=0):
	b1.move()
	px.append(b1.x)
	py.append(b1.y)
	pz.append(b1.z)
	velx.append(b1.vx)
	vely.append(b1.vy)
	velz.append(b1.vz)
	t = t+1	

print t

fig = plt.figure()
plt.title('Projectail Launch', fontsize=14)

plt.xticks(np.linspace(0, 25, 5,endpoint=True), ['', ''])
plt.yticks(np.linspace(-0.2, 1, 0.2, endpoint=True), ['', ''])
XxY=fig.add_subplot(111, xlim=(0, 25), ylim=(-0.2, 1))
plt.xlabel('$X_{(t)}$(m)')
line1, = XxY.plot([], [], 'r-', lw=2, label="XxY")

XxZ=fig.add_subplot(111, xlim=(0, 25), ylim=(-0.2, 1))
plt.ylabel('$Y_{(t)}$ e $Z_{(t)}$(m)')
plt.grid()
line2, = XxZ.plot([], [], 'b-', lw=2, label="XxZ")

def init():
	line1.set_data([],[])
	line2.set_data([],[])
	return line1, line2,
	
def animate(i):
	x=px[:i]
	y=py[:i]
	z=pz[:i]
	line1.set_data(x, y)
	line2.set_data(x, z)
	return line1, line2,
		
anim=animation.FuncAnimation(fig, animate, init_func=init, frames = 250,
interval=0, blit=True)

anim.save('Teste22.mp4', fps=30)

plt.show()
