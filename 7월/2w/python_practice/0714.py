"""
문제 14
문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
count() 메서드 사용 금지
apple # 1
banana # 3
kiwi # 0
"""
cnt=0
#word='apple'
word =list(input())
for i in range(len(word)):
    if word[i]== "a":
        cnt+=1
print(cnt)
"""
문제 15
문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
a 가 없는 경우에는 -1을 출력해주세요.
find() index() 메서드 사용 금지
banana # 1
apple # 0
kiwi # -1

문제 15.1 
문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
find() index() 메서드 사용 금지
HappyHacking # 1 6
banana # 1 3 5
kiwi # 
happyhacking
"""
#15
word =list(input())
idx=len(word)+1
for i in range(len(word)):
    if word[i]== "a":
        idx=i
if idx!=len(word)+1:
		print(idx)
else:
		print(-1)
#15.1
idx_list=[]
word =list(input())
for i in range(len(word)):
    if word[i]== "a":
        idx_list.append(i)
for j in range(len(idx_list)):
    print((idx_list[j]),end=" ")

"""
문제 16
문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
모음 : a, e, i, o, u 
count() 사용 금지
apple # 2
aeiou # 5
zxcvb # 0
"""
collection={"a":0,"e":0,"i":0,"o":0,"u":0}
word=list(input())
cnt=0
#word=list("apple")
for i in word:
    for j in collection:
        if i==j:
            cnt+=1
print(cnt)
"""
문제 17
소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
.upper(), .swapcase() 사용 금지
banana #BANANA
"""
#word="banana"
word=list(input())
word_list=[]
for i in word:
    a=chr(ord(i)-32)
    word_list.append(a)
for j in word_list:
    print("".join(j),end="")
"""
문제 18
문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
b 1
a 3
n 2
"""
word=list(input())
dic={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
for i in word:
    for j in dic:
            if i==j:
                dic[j]+=1
for k in dic:
#for k in word:
    if dic[k]!=0:
        print(k,dic[k])
