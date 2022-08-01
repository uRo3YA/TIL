#stack=[]
stack=0
while True:
    cmd=input()
    if cmd == "고무오리 디버깅 끝":
        break
    if cmd=="문제":
        stack+=1
    elif cmd=="고무오리":
        stack-=1
if stack:
    print("힝구")
else:
    print("고무오리야 사랑해")