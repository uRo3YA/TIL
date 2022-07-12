n=0
t=0
#user_input=int(input())

while True:
    try:
        user_input=int(input())
        t+=1
        n+=user_input
        print("반복횟수:",t)
        print("총합:",n)
    except EOFError:
        break