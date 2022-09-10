
import sys

sys.stdin = open("_괄호짝짓기.txt")
for tc in range(1, 11):
    N = int(input())
    arr = input()
    stack1 = []
    result = 1
    #왼쪽괄호들을 다 스택에 저장하고 오른쪽 괄호를 만난다면 pop해서 비교
    for i in range(N):
        if arr[i] == '(' or arr[i] == '{' or arr[i] == '[' or arr[i] == '<':
            stack1.append(arr[i])
        if arr[i] == ')':
            if len(stack1) > 0 and stack1.pop() != '(':
                result = 0
                break
        if arr[i] == '}':
            if len(stack1) > 0 and stack1.pop() != '{':
                result = 0
                break
        if arr[i] == ']':
            if len(stack1) > 0 and stack1.pop() != '[':
                result = 0
                break
        if arr[i] == '>':
            if len(stack1) > 0 and stack1.pop() != '<':
                result = 0
                break
    print(f"#{tc}",result)