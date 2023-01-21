n, m = map(int, input().split())
salary = list(int(x) for x in input().split())

sum = 0
for i in range(m):
    sum += salary[i]

start = 0
end = m
max_sum = sum
while end < n:
    sum = sum + salary[end] - salary[start]
    max_sum = max(max_sum, sum)
    start += 1
    end += 1
print(max_sum)