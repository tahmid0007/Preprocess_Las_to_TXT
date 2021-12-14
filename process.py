import laspy
import numpy as np
import csv
#las = laspy.read('C:/Users/mthossain/Downloads/Rhythm Garden Testing Data/CEDD Airborne LiDAR/Rhythm Garden Airborne LiDAR.las')


las = laspy.read('C:/Users/mthossain/Downloads/Rhythm Garden Testing Data/CEDD Airborne LiDAR/Rhythm Garden Airborne LiDAR.las')
header = las.header.point_count


ts1 = np.zeros((1,6))
ts2 = np.zeros((1,6))

x = np.array(las.x)
x = x - np.min(x)
y = np.array(las.y)
y = y - np.min(y)
z = np.array(las.z)
z = z - np.min(z)

r = np.array(las.red)
g = np.array(las.green)
b = np.array(las.blue)
#rgb = np.zeros((41643444,3))

rnd = np.random.choice(7327324, 100000)

#points = np.vstack((x[rnd], y[rnd], z[rnd])).transpose()
points = np.vstack((x[rnd], y[rnd], z[rnd], r[rnd], g[rnd], b[rnd])).transpose()
#points = np.vstack((x[rnd], y[rnd], z[rnd], np.ones((100000)), np.ones((100000)), np.ones((100000)))).transpose()

points = np.asarray(points)
points = points[points[:, 2].argsort()]
#points = np.sort(points, axis = 2)

#np.savetxt("p.csv", points, delimiter=",", fmt='%.3f')

#xyz = np.column_stack((x,y,z,rgb))

ts1 = points[0:50000]
ts2 = points[50000:99999]
'''for i in range(len(points)):
    if points[i][2] < 3:
        ts1 = np.concatenate((ts1, np.matrix(points[i])), axis = 0) 
    else:
        ts2 = np.concatenate((ts2, np.matrix(points[i])), axis = 0) '''
        
ts1 = np.delete(ts1, [0], 0)
ts2 = np.delete(ts2, [0], 0)

np.savetxt('./floor_1.txt', ts1, delimiter =' ',fmt='%.3f')
np.savetxt('./ceiling_1.txt', ts2, delimiter =' ',fmt='%.3f')

#data = [avg_precision*100 ,avg_recall*100, val_acc, avg_per_class_acc*100, IOU*100]
'''with open('p.csv', 'w', newline ='') as f:
    writer = csv.writer(f)
    writer.writerow(points)
    f.close()'''

#a = np.loadtxt('points.txt') 
#print(len(np.array(las.red)))