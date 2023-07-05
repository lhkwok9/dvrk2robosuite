#!/usr/bin/env python
"""Convert Recorded Data to hdf5 for Robomimic"""
import os, json, h5py, datetime
import numpy as np
from glob import glob
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
# import robosuite as suite

# from robosuite import load_controller_config

# store model xml as an attribute
# xml_path = "/home/jk/dvrk2robosuite/src/dvrk2robosuite/data_collection_test/Lift/ep_1688442425_3093536/model.xml"
# with open(xml_path, "r") as f:
#     xml_str = f.read()

# bs_data = BeautifulSoup(xml_str, "xml")

# for tag in bs_data.find_all('body', {'name':'robot0_link7'}):
#     print(tag['pos'])

tree = ET.parse('/home/jk/dvrk2robosuite/src/dvrk2robosuite/data_collection/Lift/ep_1688125683_7662618/model.xml')
root=tree.getroot()

# new = ET.Element('geom')
# new.set('name', 'robot0_link7_collision')
# new.set('type', 'mesh')
# new.set('rgba', '0 0.5 0 1')
# new.set('mesh', 'robot0_link7')

for body in root.iter('body'):
    # print(body.get('name'))
    if body.get('name') == "robot0_link7":
        # print(body.find('inertial').get('mass'))
        new=ET.SubElement(body, 'geom')
        # body.append(new)
        new.set('name', 'robot0_link7_collision')
        new.set('type', 'mesh')
        new.set('rgba', '0 0.5 0 1')
        new.set('mesh', 'robot0_link7')
        break

tree.write('output.xml')
# <body name="robot0_link7" pos="0.088 0 0" quat="0.707107 0.707107 0 0">
    # <geom name="robot0_link7_collision" type="mesh" rgba="0 0.5 0 1" mesh="robot0_link7"/>