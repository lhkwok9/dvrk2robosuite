#!/usr/bin/env python
import os, h5py
import numpy as np


file = "/home/jk/robomimic/datasets/can/mh/low_dim_v141.hdf5"
filter_key = [11, 22, 29, 30, 35, 37, 42, 5, 8, 152, 159, 179, 180, 183, 185, 188, 191, 194, 250, 259, 268, 269, 282, 286, 287, 294, 296, 205, 209, 211, 215, 226, 227, 237, 241, 242, 108, 114, 122, 124, 126, 128, 134, 139, 146, 53, 77, 82, 84, 85, 86, 87, 93, 98]

f = h5py.File('/home/jk/robomimic/datasets/can/mh/low_dim_v141.hdf5' ,'r')

for demo_name in list(f['data'].keys()):
    # if int(demo_name[5:]) in filter_key:
        print(f['data'][demo_name]['states'][0][31:33])