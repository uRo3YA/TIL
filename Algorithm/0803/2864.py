# 11 25
# 두 수의 합 중 최솟값과 최댓값을 출력한다.

# 5 -> 6
# 6 -> 5
a, b = input().split()
min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(min, max)