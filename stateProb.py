import numpy as np
import correctPair
# This function returns the probability of the
# state sequence S[T], given auc[k] and C[k][T]
# pi It is the probability of occurance of +1
# P is a 2d list containg probabilty of the states transition
# P = [[++,+-],[-+,--]]
def stateProb(S,auc,C,pi,P):
    T = len(S)
    k = len(auc)
    # P(S0....ST | 1c0T,.... k c0T)
    # = π P(ic0T|S0T) . P(S0) π_1_T P(S_i|S_i-1)
    # = P1 . P2
    # Calculating the first part
    P1 = 1
    for k in range(k):
        P1 = P1*(auc^correctPair.correctPair(C[k],S))
        
    P2 = pi
    if(S[0] == -1):
        P2 = 1-pi

    for i in range(1,T):
        if(S[i-1] == 1):
            if(S[i] == 1):
                P2 = P2 * P[0][0]
            else:
                P2 = P2 * P[0][1]
        else:
            if(S[i] == 1):
                P2 = P2 * P[1][0]
            else:
                P2 = P2 * P[1][1]            
        
    return P1*P2
    