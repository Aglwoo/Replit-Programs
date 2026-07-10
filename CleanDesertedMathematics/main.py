import numpy as np
import matplotlib.pyplot as plt
#30,9.81,20,2,0.1,0.007854,1,0.1
theta = float(input("Input the launch angle from horizontal:"))
theta = np.radians(theta)
g = float(input("Input the strength of gravity:"))
u = float(input("Input the launch speed:"))
h= float(input("Input the launch height:"))
cD = float(input("Coefficient of Drag:"))
A = float(input("Cross-sectional area:"))
dens = float(input("Air density:"))
m = float(input("Mass:"))

vx=u*np.cos(theta)
uy=u*np.sin(theta)


end=((uy+(uy**2+2*g*h)**0.5)/(g))
dt = np.linspace(0,end,300)
print(end, end*uy-0.5*g*end**2)

x1=vx*dt
y1=uy*dt-0.5*g*dt**2+h

plt.scatter(x1,y1, s=2, label="No Air Resistance")

dt=0.01

n=0
ax = 0
ay = -g
x=[0]
vx=[u*np.cos(theta)]
vy=[u*np.sin(theta)]
t=[0]
y=[h]

k=(cD*dens*A)/(2*m)


while y[n]>=0:

    v=(vx[n]**2+vy[n]**2)**0.5

    x.append(x[n] + vx[n]*dt + 0.5*ax*dt**2)
    y.append(y[n] + vy[n]*dt + 0.5*ay*dt**2)

    ax= (-(vx[n]/v)*k*v**2)/m #Has to be added to work
    ay=-g-((vy[n]/v)*k*v**2)/m #Has to be added to work

    vx.append(vx[n] + ax*dt)
    vy.append(vy[n] + ay*dt)



    t.append(t[n] + dt)

    n = n+1


plt.scatter(x,y, color="orange",s=2, label="Air Resistance")
plt.ylabel("Height / m")
plt.xlabel("x / m")
plt.legend()
plt.show()
