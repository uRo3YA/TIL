from collections import deque
def solution(s):
    s_dq = deque(s)
    stack = []
    res = True

    while s_dq:
        v = s_dq.popleft()
        if v == "(":
            stack.append(v)
        elif v == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            res = False

    return False if stack else res