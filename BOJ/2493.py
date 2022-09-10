n = int(input())
tower = list(map(int,input().split()))
answer= [0] * n
stack = []
for i in range(len(tower)):
    while stack:
        if tower[stack[-1][0]]<tower[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0]+1
            break
    stack.append((i,tower[i]))
print(*answer)
