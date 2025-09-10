import matplotlib.pyplot as plt
x1,y1=int(input("Enter x1: ")),int(input("Enter y1: "))
x2,y2=int(input("Enter x2: ")),int(input("Enter y2: "))
dx=x2-x1
dy=y2-y1
p=2*dy-dx
plt.plot(x1,y1,'ro')
while x1<x2:
    x1=x1+1
    if p<0:
        plt.plot(x1,y1,'ro')
        p=p+2*dy
    else:
        y1=y1+1
        plt.plot(x1,y1,'ro')
        p=p+2*dy-2*dx
plt.grid()
plt.show()
