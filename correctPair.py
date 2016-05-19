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
    N = n1 + l_neg*(l_neg-1)/2 - n2
    print sortedPos
    print sortedNeg
    return N


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


#test code
input_array_1 = []  #0
input_array_2 = [1] #0
input_array_3 = [1, 5]  #0
input_array_4 = [4, 1] #1
input_array_5 = [4, 1, 2, 3, 9] #3
input_array_6 = [4, 1, 3, 2, 9, 5]  #5
input_array_7 = [4, 1, 3, 2, 9, 1]  #8

#print count_inversion(input_array_1)
#print count_inversion(input_array_2)
#print count_inversion(input_array_3)
#print count_inversion(input_array_4)
#print count_inversion(input_array_5)
#print count_inversion(input_array_6)
print count_inversion(input_array_7)

a = [ 2,4,3,1,5]
b = [1,1,-1,-1,1]
print correctPair(a,b)