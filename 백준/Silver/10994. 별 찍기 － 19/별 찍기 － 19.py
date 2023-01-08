n = int(input())
for i in range(2*n-1):
    if i == 0:
        print('*'*(4*n-3))
    elif i % 2 == 1:
        print('* '*(i//2+1), end = '')
        print(' '*(4*(n-(i+1)//2)-3), end = '')
        print(' *'*(i//2+1))
    else:
        print('* '*(i//2), end = '')
        print('*'*(4*(n-(i+1)//2)-3), end = '')
        print(' *'*(i//2))
for i in range(2*n-3, -1, -1):
    if i == 0:
        print('*'*(4*n-3))
    elif i % 2 == 1:
        print('* '*(i//2+1), end = '')
        print(' '*(4*(n-(i+1)//2)-3), end = '')
        print(' *'*(i//2+1))
    else:
        print('* '*(i//2), end = '')
        print('*'*(4*(n-(i+1)//2)-3), end = '')
        print(' *'*(i//2))