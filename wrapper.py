# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:19:58 2015

@author: epnevmatikakis
"""
import numpy as np
import scipy.signal as scs
import matplotlib.pyplot as plt
from constrained_foopsi import *

np.random.seed(1200)
T = 5e3;
pr = 0.05;
sp = np.random.uniform(0,1,T)<pr
sp.astype(float)

gr = [0.95,0.8]
g = np.array([np.sum(gr),-np.prod(gr)])

c = scs.lfilter(np.array([1]),np.concatenate([np.array([1.]),-g]),sp)
sn = 2;
y = c + sn*np.random.normal(0,1,T) 

c2,b2,c12,g2,sn2,sp2 = constrained_foopsi(y)

gd_vec = np.max(np.roots(np.concatenate([np.array([1]),-g.flatten()])))**np.arange(T)
c_inferred = c2 + b2 + c12*gd_vec

plt.plot(np.arange(T),c,np.arange(T),c_inferred)

#opt.update({'p' : 1, 'bas_nonneg' : False})
#c1,b1,c11,g1,sn1,sp1 = constrained_foopsi(y, options = opt)
