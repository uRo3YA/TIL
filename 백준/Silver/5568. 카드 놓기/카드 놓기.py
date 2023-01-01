from itertools import permutations

n, k = int(input()), int(input())
cards = [input().rstrip() for _ in range(n)]
res = set()
for per in permutations(cards, k):
    res.add(''.join(per))
    
print(len(res))