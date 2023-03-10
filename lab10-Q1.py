# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:34:14 2022

@author: kagan.ozturk-ug
"""
import os
os.chdir("D:/Users/kagan.ozturk-ug/Desktop/02_Lab10_YigitKaganOzturk_22103072")
import numpy as np
import matplotlib.pyplot as plt
txt=np.loadtxt("economic_data.txt",delimiter=',')
pop=txt[:,4]
rate=txt[:,-1]
plt.plot(pop,rate,'or')
m,n=np.polyfit(pop,rate,1)
plt.plot(pop,pop*m+n,'--g')
plt.xlabel('population')
plt.ylabel('employment rate')
plt.title('relationsip between employment rate and population')

