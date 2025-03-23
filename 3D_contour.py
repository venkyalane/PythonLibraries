import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y) 

# Define a function to calculate the z values (height) based on x and y
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Calculate the z values for the meshgrid
Z = f(X, Y)

# Create a three-dimensional contour plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
contour = ax.contour3D(X, Y, Z, 50, cmap='viridis')

# Add labels and a colorbar
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
fig.colorbar(contour, ax=ax, label='Z values')

# Show the plot
plt.show()