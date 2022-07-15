# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오
# Boysenberry 3
# Blueberry 4
# Avocado 1
# Marionberry 3
# Date 9
# ...
# Melon 1
# berryfake 1

with open('python_project/data/fruits.txt', 'r',encoding="utf-8") as d:
    #word = input()
    text=d.read()
    fruit=text.split("\n")
    fruit_dict = {}

    for i in fruit:
        if i in fruit_dict:
            fruit_dict[i] += 1
        else:
            fruit_dict[i] = 1
    with open('python_project\03.txt', 'w',encoding="utf-8") as a:
        for k,v in fruit_dict.items():
             a.write(str(k)+" ")
             a.write(str(v)+"\n")