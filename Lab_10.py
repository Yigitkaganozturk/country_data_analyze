# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:20:32 2022

@author: kagan.ozturk-ug
"""

import os
os.chdir("D:/Users/kagan.ozturk-ug/Desktop/02_Lab10_YigitKaganOzturk_22103072")
import numpy as np
import matplotlib.pyplot as plt
plt.clf()
plt.figure(1)
c_names=np.loadtxt("c_names.txt",skiprows=1,dtype='str')
data=np.loadtxt("c_data.txt",skiprows=1)

fertility_under_3=np.where(data[:,0]<3)[0]
asia_countries=np.where(c_names[:,1]=='Asia')[0]
asia_data=data[asia_countries]

plt.subplot(2,2,1)
literacyFemale=100-data[:,-1]
GPD=data[:,-5]

plt.plot(GPD,literacyFemale,'p--')
plt.title('Female Literacy vs GDP')     
plt.xlabel('GDP')
plt.ylabel('Female Literacy Rate')     

plt.subplot(2,2,3)

menemp=np.mean(asia_data[:,-4])
wmenemp=np.mean(asia_data[:,-3])
sayilar=[menemp,wmenemp]
explode=[0,0.1]
names=['Male','Female']
plt.pie(sayilar, explode=explode, labels=names,autopct='%1.1f%%')
plt.title('Employment Rates by Gender in Asia')

plt.subplot(2,2,2)
infmAll=np.mean(data[:,-6])
imfmU3=np.mean(data[fertility_under_3][:,-6])
n_groups = 5


bar_width = 0.25
plt.bar('Fertility below 3',imfmU3)
plt.bar('All fertility',infmAll)
plt.ylabel('Infant mortaliity')
plt.title('Comparison of Average Infant Mortality')

plt.subplot(2,2,4)
plt.hist(GPD, 4)
plt.title('Frequency GPD for All Countries (4 bins)')

plt.figure(2)
GPDPCA=asia_data[:,-5]
names=c_names[asia_countries][:,0]
plt.plot(names,GPDPCA,'o')
plt.xticks( rotation = 45 )
plt.title('Per Capita CDP - Asian Countries')
plt.ylabel('GDP per capita')