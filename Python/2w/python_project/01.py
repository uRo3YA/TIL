# - 과일 데이터 `fruits.txt`를 활용하여 총 과일의 갯수를 `01.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.
# 출력 394
with open('July/2w/python_project/data/fruits.txt', 'r',encoding="utf-8") as d:
    lines=d.readlines()
lines=[line.rstrip('\n') for line in lines]
#print(len(lines))    
with open('July/2w/python_project/01.txt', 'w',encoding="utf-8") as a:

    a.write(str(len(lines))+"\n")
    
        
