import laspy
import numpy as np
import os
las = laspy.read('C:/Users/mthossain/Downloads/Rhythm Garden Testing Data/CEDD Airborne LiDAR/Rhythm Garden Airborne LiDAR.las')
ind = 0
k = 0


header = las.header.point_count

x = np.array(las.x)
x = x - np.min(x)
y = np.array(las.y)
y = y - np.min(y)
z = np.array(las.z)
z = z - np.min(z)

rnd = np.random.choice(header, 200000)
points = np.vstack((x[rnd], y[rnd], z[rnd])).transpose()
        
np.savetxt(("cloud.txt"), points, delimiter=" ", fmt='%.3f')





'''
points = np.loadtxt("./Annotations/powerline_1.txt")
labels = np.ones((len(points)))


from plotly.offline import plot
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import time
import numpy as np


rnd = np.random.choice(len(points), 200000)
points = points[rnd]
labels = labels[rnd]

fig = go.Figure(data=[go.Scatter3d( x=points[:,0], y=points[:,1], z=points[:,2], mode='markers', marker=dict( size=1, color=labels, colorscale='Viridis', opacity=0.8 ) )])
plot(fig) '''











