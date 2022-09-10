import sys
from collections import defaultdict
input = sys.stdin.readline
 
n = int(input())
participants = defaultdict(int)
 
for _ in range(n):
    name = input().rstrip()
    participants[name] += 1
 
for _ in range(n-1):
    name = input().rstrip()
    participants[name] -= 1
 
for key, value in participants.items():
    if value >= 1:
        print(key)