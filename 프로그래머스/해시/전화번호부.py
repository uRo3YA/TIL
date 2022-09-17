# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    num_dic={}
    answer = True
    phone_book.sort()
    for i in phone_book:
        phone=i[:2]
        if phone not in num_dic:
                num_dic[phone]=1
        else:
                num_dic[phone]+=1
        for key,value in num_dic.items():
            if value>1:
                answer=False

    return answer
a=["119", "97674223", "1195524421"]
b=["123","456","789"]
c=["12","123","1235","567","88"]
print(solution(a))
print(solution(b))
print(solution(c))
