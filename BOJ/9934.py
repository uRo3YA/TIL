# n = int(input())
# node = list(map(int, input().split()))
# check = [0] * (2**n - 1)
# tree = []

# for _ in range(n):
#     temp = []
#     flag = True
#     for i, l in enumerate(node):
#         if flag and check[i] == 0:
#             check[i] = 1
#             temp.append(l)
#             flag = False
#         elif not flag and check[i] == 0:
#             flag = True
#     tree.append(temp)

# #print(tree)
# for a in tree[::-1]:
#     print(*a)

#
x = int(input())
a = list(map(int, input().split()))
i = len(a)
while i:
    i //= 2
    print("i, i * 2 + 2:", i, i * 2 + 2)
    print(*a[i :: i * 2 + 2])  # i부터  i * 2 + 2 간격으로 슬라이스
# 3
# 6 2
# 1 4 5 7
