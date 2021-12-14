import laspy
import numpy as np
import os
#las = laspy.read('C:/Users/mthossain/Downloads/Rhythm Garden Testing Data/CEDD Airborne LiDAR/Rhythm Garden Airborne LiDAR.las')
ind = 0
k = 0
dict_class = {0: 'clutter',
        1: 'ground',
        2: 'vegetation',
        3: 'cars',
        4: 'trucks',
        5: 'powerline',
        6: 'poles',
        7: 'fences',
        8: 'buildings'
        }
pth = 'D:\\Euclideon Datasets\\dales_semantic_segmentation_las.tar\\dales_las\\train'

for object_name in os.listdir(pth):
    ind += 1

    las = laspy.read(os.path.join(pth, object_name))
    header = las.header.point_count
    
    x = np.array(las.x)
    x = x - np.min(x)
    y = np.array(las.y)
    y = y - np.min(y)
    z = np.array(las.z)
    z = z - np.min(z)
    
    rnd = np.random.choice(header, 1000000)
    labels =  np.array(las.classification)
    labels = labels[rnd]
    points = np.vstack((x[rnd], y[rnd], z[rnd], labels)).transpose()
    
    points = points[points[:, 3].argsort()]
    unique, counts = np.unique(labels, return_counts=True)
    
    labels = points[:,3]
    points = points[:,0:3]
    
    try:
        a = counts[0]
        b = counts[0] + counts[1]
        c = counts[0] + counts[1] + counts[2]
        d = counts[0] + counts[1] + counts[2] + counts[3]
        e = counts[0] + counts[1] + counts[2] + counts[3] + counts[4] 
        f = counts[0] + counts[1] + counts[2] + counts[3] + counts[4]  + counts[5]
        g = counts[0] + counts[1] + counts[2] + counts[3] + counts[4]  + counts[5] + counts[6]
        h = counts[0] + counts[1] + counts[2] + counts[3] + counts[4]  + counts[5] + counts[6] + counts[7]
        i = counts[0] + counts[1] + counts[2] + counts[3] + counts[4]  + counts[5] + counts[6] + counts[7] + counts[8]
    except:
        k += 1
        continue
    pth2 = os.path.join("./sample_" + str(ind))
    os.mkdir(pth2)
    pth3 = os.path.join("./sample_" + str(ind),"Annotations")
    os.mkdir(pth3)
            
    try:
        np.savetxt(os.path.join(pth3, "clutter_1.txt"), points[0:a], delimiter=" ", fmt='%.3f')
        np.savetxt(os.path.join(pth3, "ground_1.txt"), points[a:b], delimiter=" ", fmt='%.3f')
        np.savetxt(os.path.join(pth3, "vegetation_1.txt"), points[b:c], delimiter=" ", fmt='%.3f')
        np.savetxt(os.path.join(pth3, "cars_1.txt"), points[c:d], delimiter=" ", fmt='%.3f')
        np.savetxt(os.path.join(pth3, "trucks_1.txt"), points[d:e], delimiter=" ", fmt='%.3f')
        np.savetxt(os.path.join(pth3, "powerline_1.txt"), points[e:f], delimiter=" ", fmt='%.3f')
        np.savetxt(os.path.join(pth3, "poles_1.txt"), points[f:g], delimiter=" ", fmt='%.3f')
        np.savetxt(os.path.join(pth3, "fences_1.txt"), points[g:h], delimiter=" ", fmt='%.3f')
        np.savetxt(os.path.join(pth3, "buildings_1.txt"), points[h:i], delimiter=" ", fmt='%.3f')
    except:
        continue




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











