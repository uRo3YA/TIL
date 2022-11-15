import sys
from pprint import pprint

# sys.stdin = open("test_input.txt")
for _ in range(10):
    t = int(input())
    s = input()
    word = input()
    cnt = word.count(s)
    print(f"#{t}", cnt)
