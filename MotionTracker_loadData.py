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
#m1_d9 = load_data()

#frame_offset_right = totalframes_right-len(trackframes_right)
#data_right = np.concatenate((np.zeros(frame_offset_right), trackframes_right), 0)

#filepath_mid, data_mid, trackframes_mid, totalframes_mid = load_data()
#frame_offset_mid = totalframes_mid-len(trackframes_mid)
#data_mid = np.concatenate((np.zeros(frame_offset_mid), trackframes_mid), 0)

#NEED TO ADD OFFSET FOR FRAMES, THEN IGNORE FIRST 25*30 sec?
#frame_offset_mid = totalframes_mid-len(trackframes_mid)
#data_mid = np.concatenate((np.zeros(frame_offset_mid), trackframes_mid), 0)

temp = np.array(m1_d9[2]).astype(float)
temp2 = np.array(m1_d9[3]).astype(float)
temp3 = np.array(m1_d9[4]).astype(float)

temp[temp==0] = np.nan
temp2[temp2==0] = np.nan
temp3[temp3==0] = np.nan

temp_shift = temp+.1
temp3_shift = temp3-.1


plt.plot(temp, 'g.')
plt.plot(temp2, 'b.')
plt.plot(temp3, 'r.')
plt.ylim([0,2])
plt.title('tracked in right chamber')
plt.legend({'Right frametracker','Mid frametracker2', 'Left frametracker3'})


