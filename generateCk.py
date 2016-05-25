import correctPair
import math

def genC(S,auc):
    C = []
    for k in range(len(auc)):
        C.append( genCk(S,auc[k]) )
    return C

def genCk(S,auc_k):
    C_k = [0]
    C_k_sorted = [0]
    # S It goes from 0 to T
    T = len(S)
    N_prev = 0
    for i in range(1,T):
        N_prev = insertEle(S[:i+1],C_k,C_k_sorted,i,auc_k,N_prev)
    return C_k
    
def insertEle(subS,C_k,C_k_sorted,i,auc_k,N_prev):

    tot =  (i+1)*i/2
    # N represent the number of right pair
    N = math.ceil(tot*auc_k)
    # after inserting the i_th element the number of
    # correct pair should be greater than or equal to N
    currRight = (int)(N - N_prev)
    #print type(currRight)
    # currRight represents the number of pair right, corresponding 
    # to the element pair if one of chosen is i_th and the other one is from
    # 0 to i-1
    # hence we return N_prev + currRight as the total number of correct right pairs
    l = len (C_k_sorted)
    print i
    if(subS[i] == 1):
        if(currRight >= l):
            currRight = l
            C_k.append(C_k_sorted[-1] + 100)
            C_k_sorted.append(C_k_sorted[-1] + 100)
        else:
            data = (C_k_sorted[currRight-1] + C_k_sorted[currRight]) / 2
            C_k_sorted.insert(currRight,data)
            C_k.append(data)
    else:
        if(currRight >= l):
            currRight = l
            C_k.append(C_k_sorted[0] - 100)
            # Add the element to start 
            C_k_sorted.insert(0,C_k_sorted[0] - 100)
        else:
            data = (C_k_sorted[i-currRight-1] + C_k_sorted[i - currRight]) / 2
            C_k_sorted.insert(i-currRight,data)
            C_k.append(data)        
        
    return N_prev + currRight
# case 1    
#S = [1,1,1,1,1,1,1,1]
#auc_k = 0.7
# case 2
S = [-1,-1,-1,-1,-1,-1,-1,-1]
auc_k = 0.7
print genCk(S,auc_k)