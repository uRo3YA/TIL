while True:
    word=input()
    cnt=0
    if word=="#":
        break
    for c in word:
        if c in ['a', 'e', 'i', 'o', 'u'] or c in ['A', 'E', 'I', 'O', 'U']:
            cnt+=1
    print(cnt)