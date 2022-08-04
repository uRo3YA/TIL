list=[]
#i,j=0
#(list[i][j]==0 and list[i][j+1]==0) or (list[i][j]==0 and list[i+1][j]==0)

h_cnt=0
v_cnt=0
col=0
row=0
n=int(input())
for i in range(n): 
    list.append(input())
for i in range(n):
    v_cnt,h_cnt=0,0
    for j in range(n):
        if list[i][j]=='.':
            v_cnt+=1
        else:
            v_cnt=0
        if v_cnt==2:
                row+=1           
        if list[j][i]=='.' :
            h_cnt+=1
        else:
            h_cnt=0
        if h_cnt==2:
                col+=1
print(row, col)