from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(200000)

def find(x):
    if x == arr[x]:
        return x
    else:
        arr[x] = find(arr[x])
        return arr[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        arr[y] = x
    else:
        arr[x] = y

N, M = map(int, input().split())
arr = [i for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a, b)
else:
    print(0)