# - 과일 데이터 `fruits.txt`를 활용하여 `berry`로 끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.

with open('2회차/이태극/data/fruits.txt', 'r',encoding="utf-8") as d:
    text=d.read()
    fruit=text.split("\n")
    #fruit=text
    f_list=[]
    cnt=0
    #print(lines)
    for i in fruit:
        if i.endswith("berry") or i.endswith(" berry"):
            cnt+=1
            if i in f_list:
                continue
            else:
                f_list.append(i)
    #print(len(f_list))
    with open('2회차/이태극/02.txt', 'w',encoding="utf-8") as a:
        a.write(str(len(f_list))+"\n")
        for x in range(len(f_list)):
            a.write(f_list[x]+"\n")