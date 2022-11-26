T = int(input())
for tc in range(1, 1 + T):
    n = int(input())
    words = list(map(str, input().split()))
    median_num = n // 2
    stack = []
    idx = 1
    if n % 2 == 0:
        for q in range(n):
            if q < median_num:
                stack.append(words[q])
            else:
                stack.insert(idx, words[q])
                idx += 2
    else:
        for q in range(n):
            if q < median_num + 1:
                stack.append(words[q])
            else:
                stack.insert(idx, words[q])
                idx += 2
    print(f"#{tc}", *stack)
