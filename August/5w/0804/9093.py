n=int(input())
for i in range(n):
    word=list(input().split())
    answer=[]
    r_word=[]
    for word in word:
            r_word.append(word[::-1])

            answer= " ".join(r_word)
    print(answer)