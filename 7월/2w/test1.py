"""
문제 17
소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
.upper(), .swapcase() 사용 금지
banana #BANANA
"""
word="banana"
word_list=[]
for i in word:
    a=chr(ord(i)-32)
    word_list.append(a)
for j in word_list:
    print("".join(j),end="")