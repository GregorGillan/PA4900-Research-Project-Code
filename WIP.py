
#Testing giuthub

from vpython import *
from math import *
import numpy as np


x_axis = arrow(pos = vector(0, 0, 0), axis = vector(1, 0, 0), length = 1, color = color.red, shaftwidth = 0.05)
y_axis = arrow(pos = vector(0, 0, 0), axis = vector(0, 1, 0), length = 1, color = color.yellow, shaftwidth = 0.05)
z_axis = arrow(pos = vector(0, 0, 0), axis = vector(0, 0, 1), length = 1, color = color.green, shaftwidth = 0.05)
#Defing a particle
p1 = sphere(pos = vector(-1, 0, 0), radius = 0.1, color = color.yellow,
            vel = vector(5, 0, 0), mass = 1, charge = 1,
            make_trail = True, trail_color = color.yellow, retain = 150)
#Def mag poles
#dp1 = sphere(pos = vector(1, 0, 0), radius  = 0.2, color = color.red,
#             m = [1, 0, 0])

#Defining current loops
cLoop_1 = ring(pos=vector(-2, 0, 0), axis=vector(1, 0, 0), radius=0.5, thickness=0.05, color = color.red,
               current = 1)

cLoop_2 = ring(pos=vector(2, 0, 0), axis=vector(1 , 0, 0), radius=0.5, thickness=0.05, color = color.blue, 
               current = 1)

#dp2 = sphere(pos = vector(-1, 0, 0), radius  = 0.2, color = color.blue,
 #            m = [1, 0, 0])

#Grid of X, Y, Z components
ns = 100 #number of steps in array
X = np.linspace(-5, 5, ns)
Y = np.linspace(-5, 5, ns)
Z = np.linspace(-5, 5, ns)
X, Y, Z = np.meshgrid(X, Y, Z)
#


from vpython import *
from math import *
import numpy as np
import sys
#np.set_printoptions(threshold=sys.maxsize)


N = 11
array = np.zeros([N,3])

#defining a grid
cub_grid = np.linspace(-1, 1, N)
#array[:,0] = grid
#array[:,1] = grid
#array[:,2] = grid

x, y, z = np.meshgrid(cub_grid, cub_grid, cub_grid)

cube = x+y+z


print(cube)