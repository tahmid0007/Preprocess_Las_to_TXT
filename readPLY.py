import numpy as np
from utils.mayavi_visu import *
from plyfile import PlyData, PlyElement

plydata = PlyData.read('5080_54435.ply')
#data = read_ply('D:\\Euclideon Datasets\\dales_semantic_segmentation_ply\\dales_ply\\train\\5080_54435.ply')

xyz = np.vstack((data['x'], data['y'], data['z'])).T

rgb = np.vstack((data['red'], data['green'], data['blue'])).T

sub_labels = data['class']