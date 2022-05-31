import math as m 
import numpy as np

a1 = 1.2 #value in metres
a2 = 1.6 #value in metres
alpha1 = 0
alpha2 = 0
d1 = 0
d2 = 0
theta1 = 34
theta2 = 22

n = m.pi/180

T1 = np.array([[m.cos(theta1*n) , -m.sin(theta1*n) , 0 , a1*m.cos(theta1*n)] , 
              [m.sin(theta1*n) , m.cos(theta1*n) , 0 , a1*m.sin(theta1*n) ] , 
              [0 , 0 , 1 , 0] , 
              [0 , 0 , 0 , 1]])

T2 = np.array([[m.cos(theta2*n) , -m.sin(theta2*n) , 0 , a2*m.cos(theta2*n)] , 
              [m.sin(theta2*n) , m.cos(theta2*n) , 0 , a2*m.sin(theta2*n) ] , 
              [0 , 0 , 1 , 0] , 
              [0 , 0 , 0 , 1]])

positionmat = np.dot(T1 , T2) #calculating the dot product of matrices 

x = positionmat[0][3]
y = positionmat[1][3]

print("x = ",x)
print("y = ",y)