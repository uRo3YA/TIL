"""
문제 17
소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
.upper(), .swapcase() 사용 금지
banana #BANANA
collection={"a":0,"e":0,"i":0,"o":0,"u":0}
"""
word = input()
my_dict = {}
collection={"a":0,"e":0,"i":0,"o":0,"u":0}
for i in word:
    if i in collection:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

for k,v in my_dict.items():
    print(k, v)
