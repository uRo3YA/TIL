def solution(sizes):
    big=[]
    small=[]
    for i in sizes:
        if i[0]>i[1]:
            big.append(i[0])
            small.append(i[1])
        else:
            big.append(i[1])
            small.append(i[0])
            
    return max(big)*max(small)
