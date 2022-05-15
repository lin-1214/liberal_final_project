from vpython import *
import numpy as np

#code

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
    rate(1)
        
        













# #parameters

# #比生長率最大值
# u_max=

# #制限基質濃度
# S=

# #飽和常數  u=u_max/2時之S
# K_s=

# #Monod equation
# u=(u_max*S)/(K_s+S)
