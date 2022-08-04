m = int(input())

data = [1, 0, 0]
for _ in range(m) :
  x, y = map(int, input().split())
  data[x-1], data[y-1] = data[y-1], data[x-1]

for i in range(3) :
  if data[i] == 1 :
    print(i + 1)