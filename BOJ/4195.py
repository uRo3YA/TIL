parents = {}
counter = {}


def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a
        counter[a] += counter[b]


for _ in range(int(input())):
    for i in range(int(input())):
        a, b = input().split()

        if a not in parents:
            parents[a] = a
            counter[a] = 1
        if b not in parents:
            parents[b] = b
            counter[b] = 1

        union(a, b)

        print(counter[find(a)])