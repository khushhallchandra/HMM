import numpy as np

# pi It is the probability of occurance of +1
# P is a 2d list containg probabilty of the states transition
# P = [[++,+-],[-+,--]]
# We have only 2 posible states, hence 4 possible transitions
# T is the length of state sequence
# The states are represented by numbers -1 and +1
# The function returns a list of length T

def genSeq(pi,P,T):
    preState = 1
    r = np.random.uniform(0,1)
    if(r>=pi):
        preState = -1
    r = np.random.uniform(0,1,T-1)
    seq = [preState]
    for i in range(T-1):
        if(preState==1):
            seq.append(genState(P[0][0],r[i]))
        else:
            seq.append(genState(P[1][0],r[i]))
        preState = seq[i+1]
    return seq
    
def genState(P,r):
    if(r<P):
        return 1
    else:
        return -1