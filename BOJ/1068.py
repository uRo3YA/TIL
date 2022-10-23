def dfs(num, arr):
    arr[num] = -51
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)


n = int(input())  # n<=50
arr = list(map(int, input().split()))  # 각 노드의 부모가 주어진다.
k = int(input())
count = 0

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -51:
        if i not in arr:
            count += 1
print(count)
# 재귀가 끝나면 삭제될 노드들은 전부 -51로 갱신되어있으므로,
# -51가 아니면서, 다른 노드의 부모노드도 아닌 원소를 찾을 때마다 count를 1씩 늘린다.
