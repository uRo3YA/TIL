def solution(survey, choices):
    answer = ''
    scores = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0 }
    add_score = {1:-3, 2:-2, 3:-1, 4:0, 5:1, 6:2, 7:3}

    for i in range(len(survey)):
        scores[survey[i][0]] += add_score[choices[i]]
    # {'R': 3, 'T': 0, 'C': -1, 'F': 0, 'J': 0, 'M': -2, 'A': 1, 'N': 1}
    
    #1번 유형
    if scores["R"] <= scores["T"]:
        answer+="R"
    else:
        answer+="T"
    #2번 유형
    if scores["C"] <= scores["F"]:
        answer+="C"
    else:
        answer+="F"
    #3번 유형
    if scores["J"] <= scores["M"]:
        answer+="J"
    else:
        answer+="M"
    #4번 유형
    if scores["A"] <= scores["N"]:
        answer+="A"
    else:
        answer+="N"
    # print(answer)
    # print(scores)
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))

#"TCMA"
#an 5 => n+1
#cf 3 => c+1
#mj 2 => m+2
#tj 7 => t+3
#na 5 => n+1
#t3cm

