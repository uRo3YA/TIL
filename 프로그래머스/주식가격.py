from collections import deque

def solution(prices):
    answer = []
    stock=deque(prices)
    while len(stock)>0:
        now=stock[0]
        stock.popleft()
        cnt=0
        for i in stock:
            cnt+=1
            if now > i:  
                break
        answer.append(cnt)
    return answer

print(solution([1, 2, 3, 2, 3]))  