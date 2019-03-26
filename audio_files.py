# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:00:01 2019

@author: Rohan
"""
from scipy.io import wavfile
import numpy as np
fs, a = wavfile.read('audio1.wav')
fs1, b = wavfile.read('audio2.wav')

n = min(len(a), len(b))
match = np.flatnonzero(a[:n] == b[:n])
x= match.size
if len(a) > len(b):
    total_elements = np.multiply(*a.shape)
else:
    total_elements = np.multiply(*b.shape)
percentage = x/total_elements
print('{:.3f}% Match'.format(percentage*100))