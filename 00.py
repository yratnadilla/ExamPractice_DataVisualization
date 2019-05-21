import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# solve linear equations
a = np.array([
    [1, -2, 1],
    [3, 1, -2],
    [7, -6, -1]
])

b = np.array([6, 4, 10])

c = np.linalg.solve(a, b)

# plot equations
x1 = np.array([[a[0][0] * c[0], 0, 0]])
y1 = np.array([[0, a[0][1] * c[1], 0]])
z1 = np.array([[0, 0, a[0][2] * c[2]]])

x2 = np.array([a[1][0] * c[0], 0, 0])
y2 = np.array([0, a[1][1] * c[1], 0])
z2 = np.array([[0, 0, a[1][2] * c[2]]])

x3 = np.array([a[2][0] * c[0], 0, 0])
y3 = np.array([0, a[2][1] * c[1], 0])
z3 = np.array([[0, 0, a[2][2] * c[2]]])

plt.figure('Plot Result')

# plot 1
plot1 = plt.subplot(131, projection = '3d')
plot1.scatter(x1, y1, z1, color = 'red')
plot1.plot_wireframe(x1, y1, z1, facecolors = 'green', alpha = 0.3)
plot1.set_xlabel('x-value')
plot1.set_ylabel('y-value')
plot1.set_zlabel('z-value')

# plot 2
plot2 = plt.subplot(132, projection = '3d')
plot2.scatter(x2, y2, z2, color = 'green')
plot2.plot_wireframe(x2, y2, z2, facecolors = 'blue', alpha = 0.3)
plot2.set_xlabel('x-value')
plot2.set_ylabel('y-value')
plot2.set_zlabel('z-value')

# plot 3
plot3 = plt.subplot(133, projection = '3d')
plot3.scatter(x3, y3, z3, color = 'blue')
plot3.plot_wireframe(x3, y3, z3, facecolors = 'red', alpha = 0.3)
plot3.set_xlabel('x-value')
plot3.set_ylabel('y-value')
plot3.set_zlabel('z-value')

plt.show()