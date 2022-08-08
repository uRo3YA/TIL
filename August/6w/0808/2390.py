nan_list=[]
nan_sum=0
for _ in range(9):
   a=int(input())
   nan_list.append(a)
   nan_sum+=a
f_nan_sum=nan_sum-100

### 가짜 찾기
for i in range(9):
  a1=int(nan_list[i])
  for j in range(9):
      a2=int(nan_list[j])  
      if f_nan_sum == (a1+a2):
          num1=nan_list[i]
          num2=nan_list[j]
          #print("a1:",a1)
          #print("a2:",a2)
          break
### 리스트에서 제거 후 정렬
nan_list.remove(num1)
nan_list.remove(num2)
nan_list.sort()
### 출력
for i in range(len(nan_list)):
    print(nan_list[i])


