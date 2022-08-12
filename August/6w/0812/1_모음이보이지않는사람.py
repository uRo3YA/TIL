import sys

sys.stdin = open("_모음이보이지않는사람.txt")
chk="aeiou"
T = int(input())
for tc in range(1, T+1):
    S = list(map(str, input()))
    word=""
    for c in S:
        if c not in chk:
            word+=c
    print(f"#{tc}",word)    