# plotting normal distribution
import pylab
from pomegranate import *
import matplotlib as plt
data = NormalDistribution(0,1)
plt.figure(figsize = (10,5))
data.plot(n=100000,edgecolor='c',facecolor='c',alpha=1,bins=200)
