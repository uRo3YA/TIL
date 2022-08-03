# 첫째 줄에 배열의 크기 N, M
# 다음 N개의 줄에는 M개의 정수로 배열이 주어진다.
# 그 다음 줄에는 합을 구할 부분의 개수 K
# 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다
# 2 3
# 1 2 4
# 8 16 32
# 3
# 1 1 2 3 63
# 1 2 1 2
# 1 3 2 3
#(i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합

import sys
input=sys.stdin.readline
mat1=[]
matrix=[]
n,m=map(int,input().split())
for _ in range(n):
    #line=list(map(int,input().split()))
    line=tuple(map(int,input().split()))
    mat1.append(line)
k=int(input())

matrix=mat1
print(matrix)
for _ in range(k):
    i,j,x,y=map(int,input().split())
    sum_=0
#     # 접근방법 1 // 시간초과
#     # 순회하며 합 구하기
#     # for a in range(i-1,x):
#     #     for b in range(j-1,y):
#     #         sum_+=mat1[a][b]
#     # print(sum_)
    
    # 접근방법 2 //틀림, 인덱스 에러
    # 슬라이싱 해서 합 구하기
    #matrix=[n[j-1:j+y-1] for n in mat1[i-1:i+x-1]]
    for a in range(i-1,x):
        sum_+=sum(matrix[a][j-1:y])
    print(sum_)

# import sys
# input = sys.stdin.readline
 
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# memo = [[0] * (m+1) for _ in range(n+1)]
 
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         memo[i][j] = arr[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1]
 
# k = int(input())
# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])