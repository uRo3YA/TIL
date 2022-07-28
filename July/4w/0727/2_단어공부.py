s=input().upper()
s_list=list(set(s))
cnt=[]
#print(s_list)
for i in s_list:       
    count = s.count(i)
    #print(count)
    cnt.append(count)    

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
   print(s_list[(cnt.index(max(cnt)))])