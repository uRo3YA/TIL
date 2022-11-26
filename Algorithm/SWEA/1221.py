import sys

sys.stdin = open("1221.txt")
c = int(input())
for tc in range(1, c + 1):
    a, b = input().split()
    arr = list(input().split())
    word = []
    dic = {
        # "ZRO": 0,
        # "ONE": 0,
        # "TWO": 0,
        # "THR": 0,
        # "FOR": 0,
        # "FIV": 0,
        # "SIX": 0,
        # "SVN": 0,
        # "EGT": 0,
        # "NIN": 0,
    }
    for x in arr:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 0

    for key, val in dic.items():
        for y in range(val):
            word.append(key)
    print(f"#{tc}")
    print(*word)
