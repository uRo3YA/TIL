# 아래의 내용을  00.txt에 기록하시오.
# N회차 홍길동
# Hello, Python!
# 1일차 파이썬 공부 중
# 2일차 파이썬 공부 중
# 3일차 파이썬 공부 중
# 4일차 파이썬 공부 중
# 5일차 파이썬 공부 중
with open('python_project/00.txt', 'w',encoding="utf-8") as d:
    print("회차와 이름을 입력하시오:",end="")
    n,m=input().split()
    d.write(f"{int(n)}회차 {m}\n")
    for i in range(5):
        d.write(f"{i+1}일차 파이썬 공부중\n")