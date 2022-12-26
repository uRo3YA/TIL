m = int(input())

def binary(start, end, m):
    while start <= end:
        mid = (start + end) // 2 
        num = mid * 5          
        count = 0              
        i = 5       
        while i <= num:          
            count += num // i
            i *= 5 
        if count == m:
            return mid * 5
        elif count < m:
            start = mid+1
        else:
            end = mid-1
    return -1

print(binary(1, m, m))