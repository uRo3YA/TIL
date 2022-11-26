import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


def solve(arr):
    while len(arr) != 1:
        arr.append(lcm(arr.pop(), arr.pop()))
    return arr[0]


def solution(arr):
    answer = solve(arr)
    return answer


print(solution([1, 2, 3]))
print(solution([2, 6, 8, 14]))
