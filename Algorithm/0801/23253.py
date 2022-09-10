# 4 2
# 2
# 3 1
# 2
# 4 2

#교과서 N 더미 M
#첫번째 더미
#3번책 1번책
#두번째 더미 
#4번책 2번책

n,m=map(int,input().split())
book_stack=[]
for i in range(m):
    x=int(input())
    book=list(map(int,input().split()))
    for j in book:
        book_stack.append(j)
print(book_stack)
