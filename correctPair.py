# 2 4 3 1 3
# + + - - +
# The function takes one of the
# componenent of C say C_k and state sequence
def correctPair(C_k,S):
    C_k_pos = []
    C_k_neg = []
    l = len(S)
    for i in range(l):
        if(S[i] == 1):
            C_k_pos.append(C_k[i])
        else:
            C_k_neg.append(C_k[i])
    l_pos = len(C_k_pos)
    l_neg = len(C_k_neg)
    sortedPos,n1 = count_inversion(C_k_pos)
    sortedNeg,n2 = count_inversion(C_k_neg)
    #print sortedPos
    #print sortedNeg
    
    n3 = 0
    i = 0
    count = 0
    for item in sortedNeg:
        for j in range(i,l_pos):
            if(item <= sortedPos[j]):
                break
            else:
                count += 1
        i = count
        n3 += count
    # n1 represents the no. of inversion considering less than or equal to
    N = n1 + l_neg*(l_neg-1)/2 - n2 +n3
    #print n3 
    return l*(l-1)/2 - N


def count_inversion(lst):
    return merge_count_inversion(lst)

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count        


a = [ 2,4,3,1,5]
b = [1,1,-1,-1,1]
print correctPair(a,b)