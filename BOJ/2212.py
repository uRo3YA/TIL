n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

## k>n일때 예외처리
if k >= n:
    print(0)
else:
    sensor.sort()
    gap = []
    for i in range(1, n):
        gap.append((sensor[i] - sensor[i - 1], i))
    gap.sort()

    standard = [0]
    result = 0
    for i in range(k - 1):
        standard.append(gap.pop()[1])
    standard.append(0)

    result = 0
    for i in range(k):  # 0, 1
        result += sensor[standard[i + 1] - 1] - sensor[standard[i]]
    print(result)
