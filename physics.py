import math
from vpython import *
# Web VPython 3.2

R = 0.1
theta = 0
phi = 0
dtheta = pi/16
dphi = 2*pi/32
area = []
A = 3
k = 9e9
ep = 1/(4*pi*k)
qq = 1.5e-8
q1 = sphere(pos=vector(.5*R,0.2*R,0),radius=R/60, color=color.yellow,q=qq)
q2 = sphere(pos=vector(-.5*R,0.2*R,0),radius=R/60, color=color.cyan,q=-qq)

def E(rqt,rot):
  r = rot - rqt.pos
  Et = k*rqt.q*norm(r)/mag(r)**2
  return(Et)
while phi<2*pi:
  theta = 0
  while theta<pi:
    rt = vector(R*sin(theta)*cos(phi),R*sin(theta)*sin(phi),R*cos(theta))
    dltheta = R*dtheta
    dlphi = R*sin(theta)*dphi
    Asmall = dltheta*dlphi
    Rsmall = sqrt(Asmall/pi)
    area = area + [cylinder(pos=rt,axis=(R/100)*norm(rt),radius=Rsmall,opacity=0.3,color=color.white,dA = dltheta*dlphi)]
    theta = theta + dtheta
  phi = phi + dphi

Escale = 1e-6
Phi = 0
for a in area:
  Ed = E(q1,a.pos) + E(q2,a.pos)
  dPhi = dot(Ed,norm(a.axis))*a.dA
  Phi = Phi + dPhi
  if dPhi>0:
    a.color=color.red
  if dPhi<0:
    a.color=color.blue
  arrow(pos=a.pos,axis=Escale*Ed,color=color.yellow)
  
print("Phi = ",Phi)
print("q/ep  = ",q1.q/ep)
  
while True:
    rate(30)  
  