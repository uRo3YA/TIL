id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

# def solution(id_list, report, k):
#     answer = []
#     return answer
def solution(id_list, report, k):
    report = set(report)
    answer = {x:0 for x in id_list } 
    
    reports = {x:0 for x in id_list}
    for x in report :
        reports[x.split()[1]]+=1
        
    for x in report : 
        if reports[x.split()[1]] >= k :
            answer[x.split()[0]] +=1
        
    return list(answer.values())
