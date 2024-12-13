# import numpy as np
# from scipy import stats
# data = np.array([[1, 4, 3], [2, .6, 1.2], [2, 1, 1.2],
#          [2, 0.5, 1.4], [5, .5, 0], [0, 0, 0],
#          [1, 4, 3], [5, .5, 0], [2, .5, 1.2]])
#
# data = data.T #The KDE takes N vectors of length K for K data points
#               #rather than K vectors of length N
#
# kde = stats.gaussian_kde(data)
# print("kde: ", kde)
#
# # You now have your kde!!  Interpreting it / visualising it can be difficult with 3D data
# # You might like to try 2D data first - then you can plot the resulting estimated pdf
# # as the height in the third dimension, making visualisation easier.
#
# # Here is the basic way to evaluate the estimated pdf on a regular n-dimensional mesh
# # Create a regular N-dimensional grid with (arbitrary) 20 points in each dimension
# minima = data.T.min(axis=0)
# maxima = data.T.max(axis=0)
# space = [np.linspace(mini,maxi,20) for mini, maxi in zip(minima,maxima)]
# grid = np.meshgrid(*space)
#
# #Turn the grid into N-dimensional coordinates for each point
# #Note - coords will get very large as N increases...
# coords = np.vstack(list(map(np.ravel, grid)))
#
# #Evaluate the KD estimated pdf at each coordinate
# density = kde(coords)
#
# print("density: ", density)
#
# #Do what you like with the density values here..
# #plot them, output them, use them elsewhere...


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

data = np.array([[1, 4, 3], [2, .6, 1.2], [2, 1, 1.2],
         [2, 0.5, 1.4], [5, .5, 0], [0, 0, 0],
         [1, 4, 3], [5, .5, 0], [2, .5, 1.2]])
data = data.T

##############################################################
## in case of sklearn we can use ##
# using grid search cross-validation to optimize the bandwidth
# params = {'bandwidth': np.logspace(-1, 1, 20)}
# grid = GridSearchCV(KernelDensity(), params)
# grid.fit(data)
# print("best bandwidth: {0}".format(grid.best_estimator_.bandwidth))
## how to use this with scipy KDE() ?########
##############################################################

kde = stats.gaussian_kde(data)

# Here is the basic way to evaluate the estimated pdf on a regular n-dimensional mesh
# Create a regular N-dimensional grid with (arbitrary) 20 points in each dimension
minima = data.T.min(axis=0)
maxima = data.T.max(axis=0)
space = [np.linspace(mini,maxi,20) for mini, maxi in zip(minima,maxima)]
grid = np.meshgrid(*space)

#Turn the grid into N-dimensional coordinates for each point
#Note - coords will get very large as N increases...
# coords = np.vstack(map(np.ravel, grid))
coords = np.vstack(grid)

#Evaluate the KD estimated pdf at each coordinate
# density = kde(coords)
x, y, z = data
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.contour(x, y, z, zdir='x', offset=-40, cmap=cm.coolwarm)
## not wroking ###
plt.show()