import matplotlib.pyplot as plt

x1=int(input("enter the value of x1:"))
y1=int(input("enter the value of y1:"))
x2=int(input("enter the value of x2:"))
y2=int(input("enter the value of y2:"))

dx=abs(x2-x1)
dy=abs(y2-y1)

steps=max(dx,dy)

x_increment=dx/steps
y_increment=dy/steps

x_points=[x1]
y_points=[y1]
plt.plot(x1,y1,'ro')
for i in range(steps):
    x1=x1+x_increment
    y1=y1+y_increment
    x_points.append(x1)
    y_points.append(y1)
plt.plot(x_points,y_points, marker='o')
plt.show()
