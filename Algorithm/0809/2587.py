data=[]
for _ in range(5) :
  data.append(int(input()))
avg = sum(data) // 5
data.sort()
print(avg)
print(data[2])