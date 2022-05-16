from vpython import *
import numpy as np
#Theme: Growth of E. coli

#parameters：
t=0
dt=0.001

#initial cell & substrate concentration
C_c,C_s=1e-5,100
#growth & death rate
r_g,r_d=0,0

#maximum vslue of specific growth rate(/h)
u_max=1.3

#subtration constant, equal to the concentration of subtrate giving growth rate of u_max(g/L)
K_s=2.2e-5

#death constant(/h)
k_d=0.02

scene_plot = graph(height = 400, width = 800,align = 'left', xtitle='t', ytitle='cell concentration', background=vector(0.2, 0.6, 0.2))
cc=gcurve(color=color.blue,graph=scene_plot)

#equations
while True:
    rate(1000)
    t+=dt
    dC_c=(r_g-r_d)*dt
    dC_s=-r_g*dt
    C_c+=dC_c
    C_s+=dC_s
    r_g=u_max*C_s*C_c/(K_s+C_s) #monod equation
    r_d=k_d*C_c
    #print(C_c)
    
    cc.plot(t,C_c)
    if (C_c >= 0.4):
        print("Final cell concentration:",C_c)
        break
'''
#initial variable set up
sample_i=5
plate_radius=0.1 #centimeter
sample_radius=0.0005
sample_num=sample_i

sample=[]
pos_array=[]
t=0
dt=0.001

max_life=10
dis_after_grow=sample_radius*3

#function array to vector
def a_to_v(a):
    return vector(a[0], a[1], a[2])

#set up plate

scene = canvas(width=800, height=800, background=vector(0.85, 0.85, 0.85), center=vec(0,0,0))
plate = cylinder(color=vec(255/256,218/256,185/256), radius= plate_radius, pos=vec(0,0,0), opacity=0.5, axis=vec(0,0,-plate_radius/20))
side_of_plate=ring(color=vec(255/256,218/256,185/256), radius= plate_radius, pos=vec(0,0,0), opacity=0.5, length=plate_radius/10,axis=vec(0,0,-plate_radius/10), thickness=0.001)

#set up sample
#using uniform distribution (polar coordinate: 2 variable (r, theta))
r=np.random.rand(sample_i)*plate_radius
theta=np.random.rand(sample_i)*2*pi

#!!!!!!!!!!!!!!!find numpy elementwise calculation!!!!!!!!!!!!!!!
#using np.multiply(array1, array2), np.cos(), np.sin()

pos_array.append(np.multiply(r,np.cos(theta)))
pos_array.append(np.multiply(r,np.sin(theta)))
pos_array.append(np.zeros(sample_i))
pos_array=np.transpose(pos_array)

for i in range(sample_i):
    ball=sphere(radius=sample_radius, pos=a_to_v(pos_array[i]), color=color.blue, life=0)
    sample.append(ball)

#function of growing
def grow(i):
    return
    

#growing part
while True:
    rate(1000)
    t+=dt
    print("Period:", i+1)

    for i in range(sample_num):
        if(sample[i].life<max_life):
            sample[i].life+=1
            theta=np.random.rand()*2*pi
            if mag(sample[i].pos+vec(dis_after_grow*cos(theta), dis_after_grow*sin(theta),0)) >= plate_radius :
                theta=np.random.rand()*2*pi
            ball=sphere(radius=sample_radius, pos=sample[i].pos+vec(dis_after_grow*cos(theta), dis_after_grow*sin(theta),0), color=color.blue, life=0)
            sample.append(ball)
            sample_num+=1
'''
    

        
        












