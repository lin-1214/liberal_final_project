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
food_rate=1000



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

#set up plot

scene1=graph(width=400, height=400, background=vector(0.85, 0.85, 0.85))
func1=gcurve(graph=scene1, color=color.blue)

#!!!!!!!!!!!!!!!find numpy elementwise calculation!!!!!!!!!!!!!!!
#using np.multiply(array1, array2), np.cos(), np.sin()

pos_array.append(np.multiply(r,np.cos(theta)))
pos_array.append(np.multiply(r,np.sin(theta)))
pos_array.append(np.zeros(sample_i))
pos_array=np.transpose(pos_array)

for i in range(sample_i):
    ball=sphere(radius=sample_radius, pos=a_to_v(pos_array[i]), color=color.blue, eat=False, ate=True)
    sample.append(ball)

#function of growing

def discuss_die(a, b):
    num=b
    for i in range(len(a)-1, 0, -1):
        if not a[i].eat and not a[i].ate:
            del a[i]
            num=num-1
        else:
            a[i].ate=a[i].eat
            a[i].eat=False
    return num

def feed(a, num):
    for i in range(food_rate):
        where=np.random.randint(0,int(num)-1)
        if not a[where].eat :
            a[where].eat=True
    return

def grow(a, b):
    num=b
    for i in range(len(a)):
        if a[i].eat and a[i].ate:
            theta=np.random.rand()*2*pi
            if mag(sample[i].pos+vec(dis_after_grow*cos(theta), dis_after_grow*sin(theta),0)) >= plate_radius :
                theta=np.random.rand()*2*pi
            ball=sphere(radius=sample_radius, pos=sample[i].pos+vec(dis_after_grow*cos(theta), dis_after_grow*sin(theta),0), color=color.blue, life=0, eat=False, ate=True)
            sample.append(ball)
            num=num+1   
    return num
    

#growing part

t=0

while True:
    #print("Period:", i+1)

    feed(sample, sample_num)
    
    sample_num=grow(sample, sample_num)

    sample_num=discuss_die(sample, sample_num)

    func1.plot(pos=(t,sample_num))
    t+=1

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
