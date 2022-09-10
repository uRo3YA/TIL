

for _ in range(3):
    string = input()
    answer, cnt = 1, 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            cnt += 1
            if cnt > answer:
                answer = cnt
        else:
            cnt = 1
    print(answer)