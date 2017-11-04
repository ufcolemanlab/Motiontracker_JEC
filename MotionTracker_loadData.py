# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:43:58 2017

@author: jcoleman
"""

import Tkinter as tk
import tkFileDialog
import pickle
import os
import numpy as np
from matplotlib import pyplot as plt


# Load data fro right(R) chamber
def load_data():
    
    root = tk.Tk()
    root.withdraw()
    root.update()
    file_path = tkFileDialog.askopenfilename(parent=root,title='Choose a pickle file ...')
    
    with open(file_path) as f:  # Python 3: open(..., 'rb')
        alldata = pickle.load(f)
        a = alldata['frametracker']
        b = alldata['frametracker2']
        c = alldata['frametracker3']
        d = alldata['frameNumber']
        #pad with nans/zeros to align frames (frameNumber - len(a))
        
    return file_path, alldata, a, b, c, d

    
## Check data
#filepath_right, data_right, trackframes_right, totalframes_right = load_data()
#frame_offset_right = totalframes_right-len(trackframes_right)
#data_right = np.concatenate((np.zeros(frame_offset_right), trackframes_right), 0)

#filepath_mid, data_mid, trackframes_mid, totalframes_mid = load_data()
#frame_offset_mid = totalframes_mid-len(trackframes_mid)
#data_mid = np.concatenate((np.zeros(frame_offset_mid), trackframes_mid), 0)

#NEED TO ADD OFFSET FOR FRAMES, THEN IGNORE FIRST 25*30 sec?
#frame_offset_mid = totalframes_mid-len(trackframes_mid)
#data_mid = np.concatenate((np.zeros(frame_offset_mid), trackframes_mid), 0)

data_rightShift = np.array(frametracker)+1
data_leftShift = np.array(frametracker3)-1

plt.plot(frametracker, 'g')
plt.plot(frametracker2, 'b')
plt.plot(frametracker3, 'r')
plt.ylim([-2,4])
plt.title('tracked in right chamber')
plt.legend({'Right frametracker','Mid frametracker2', 'Left frametracker3'})


