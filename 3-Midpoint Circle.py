import matplotlib.pyplot as plt
x_center, y_center = int(input("enter the x-coordinate of the center: ")), int(input("enter the y-coordinate of the center: "))
r = int(input("enter radius: "))
p = 1.25 - r
x0 = 0
y0 = r
while(x0 < y0):
  plt.plot(x_center + x0, y_center + y0, 'ro')
  plt.plot(x_center - x0, y_center + y0, 'ro')
  plt.plot(x_center - x0, y_center - y0, 'ro')
  plt.plot(x_center + x0, y_center - y0, 'ro')
  plt.plot(x_center + y0, y_center + x0, 'ro')
  plt.plot(x_center - y0, y_center + x0, 'ro')
  plt.plot(x_center + y0, y_center - x0, 'ro')
  plt.plot(x_center - y0, y_center - x0, 'ro')
  x0 += 1
  if p < 0:
    p = p + 2 * x0 + 1
  else:
    y0 -= 1
    p = p + 2 * x0 - 2 * y0 + 1

plt.grid()
plt.show()
