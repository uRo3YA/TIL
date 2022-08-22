text = input()
s = set()
for i in range(len(text)):
    for j in range(i, len(text)):
        s.add(text[i:j+1])
print(len(s))