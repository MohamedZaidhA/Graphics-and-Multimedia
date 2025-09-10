import matplotlib.pyplot as plt

def midpoint_ellipse(r1, r2, xc, yc):
    x = 0
    y = r2
    rx2= r1**2
    ry2 = r2**2
    p1 = ry2 - rx2 * r2 + 0.25 * rx2

    while (2 * ry2 * x) < (2 * rx2 * y):
        plt.plot(xc + x, yc + y, 'ro')
        plt.plot(xc - x, yc + y, 'ro')
        plt.plot(xc + x, yc - y, 'ro')
        plt.plot(xc - x, yc - y, 'ro')

        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2

    p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2
    while y >= 0:
        plt.plot(xc + x, yc + y, 'ro')
        plt.plot(xc - x, yc + y, 'ro')
        plt.plot(xc + x, yc - y, 'ro')
        plt.plot(xc - x, yc - y, 'ro')

        y -= 1
        if p2 > 0:
            p2 += -2 * rx2 * y + rx2
        else:
            x += 1
            p2 += 2 * ry2 * x - 2 * rx2 * y + rx2

r1 = int(input("Enter the first radius: "))
r2 = int(input("Enter the second radius: "))
xc = int(input("Enter the x coordinate of the center: "))
yc = int(input("Enter the y coordinate of the center: "))
plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.title('Midpoint Ellipse')
midpoint_ellipse(r1, r2, xc, yc)
plt.grid()
plt.show()
