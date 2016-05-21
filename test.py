sortedPos = [2,4,5]
sortedNeg = [3,4.5,50]
l_pos = len(sortedPos)
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

print n3       