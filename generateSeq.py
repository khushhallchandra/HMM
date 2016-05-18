import numpy as np

# P is a list containg probabilty of the states 
# P = [p1,p2]
# p1 probability for +1
# We have only 2 posible states
# T is the length of state sequence
# The states are represented by numbers -1 and 1
# The function returns a numpy array of length T
def genSeq(P,T):
    #P = np.array(P)
    #P = np.sort(P)
    r = np.random.uniform(0,1,T)
    vecS = np.vectorize(randGen) 
    return vecS(P[0], r)
    
def randGen(P,r):
    #r = np.random.uniform(0,1)
    if(P<r):
        return 1
    else:
        return -1
print "Done"
a = [0.4,0.6]
S = genSeq(a,500)