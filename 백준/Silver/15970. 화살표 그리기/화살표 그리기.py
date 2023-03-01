def dist(arr):
    sum = 0
    for i in range(len(arr)):
        if i == 0:
            sum += arr[1] - arr[0]
        elif i == len(arr) - 1:
            sum += arr[len(arr) - 1] - arr[len(arr) - 2]
        else:
            if arr[i + 1] - arr[i] >= arr[i] - arr[i - 1]:
                sum += arr[i] - arr[i - 1]
            else:
                sum += arr[i + 1] - arr[i]
    return sum

ans = 0
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([b, a])
arr.sort()
l = arr[-1][0]
for i in range(1, l+1):
    x = []
    for j in range(n):
        if arr[j][0] == i:
            x.append(arr[j][1])
    ans += dist(x)
print(ans)