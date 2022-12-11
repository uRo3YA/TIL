n = int(input())
dic = {}
for i in range(n):
    dic[i+1] = int(input())

while True:
    baseSet = set(dic.values())
    print("baseSet:",baseSet)
    #딕셔너리 재정의
    dic = {key:value for key, value in dic.items() if key in baseSet}
    print("dic:",dic)
    print("set(dic.values())",set(dic.values()))
    if baseSet == set(dic.values()):
        break
print(len(dic))
for key in dic.keys():
    print(key)