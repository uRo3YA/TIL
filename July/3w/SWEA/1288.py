t=int(input())
for x in range(t):
    n=int(input())
    num=[0]*10
    i=1
    while 0 in num:
        nums=str((n)*i)
        for j in range(len(nums)):
            num[int(nums[j])]+=1
        i+=1
    print(f"#{x+1}",nums)




