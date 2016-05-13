# plotting normal distribution
from pomegranate import *
from matplotlib import pyplot as plt
data = NormalDistribution(0,1)
plt.figure(figsize=(10,8))
data.plot(n=100000,edgecolor='c',facecolor='c',alpha=1,bins=200)
plt.show()