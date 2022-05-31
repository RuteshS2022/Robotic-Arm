import math as m 

l1 = float(input("length of the link 1 is "))
l2 = float(input("length of the link 2 is "))
theta1 = float(input("rotation angle (in degrees) of the first link is "))
theta2 = float(input("rotation angle (in degrees) of the second link is "))

n = m.pi/180

x = (l1*m.cos(theta1*n)) + (l2*m.cos((theta1+theta2)*n))
y = (l1*m.sin(theta1*n)) + (l2*m.sin((theta1+theta2)*n))

print("x = ",x)
print("y = ",y)