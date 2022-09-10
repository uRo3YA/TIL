a=[]
b=[]
for i in range(10):
    a.append(int(input()))
for i in range(10):
    b.append(int(input()))
a.sort(reverse=True)
b.sort(reverse=True)
sum_a,sum_b=0,0
for i in range(3):
    sum_a+=a[i]
    sum_b+=b[i]
print(sum_a,sum_b)
