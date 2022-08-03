cnt=0
board = []

for i in range(8) :
    board.append(list(map(str, input())))
result = 0
for i in range(8) :
    for j in range(8) :
        
        if (i+j) % 2 ==0 :
            #(0,0), (0,2)....
            #(1,1), (1,3)
            if board[i][j]=='F':         
                result += 1

print(result)