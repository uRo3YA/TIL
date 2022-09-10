def solution(absolutes, signs):
    answer=0
    for i in range(len(signs)):
        if signs[i]==True:
            answer+=absolutes[i] 
        else:
            answer-=absolutes[i] 
    return answer

# [4,7,12]	[true,false,true]	9
# [1,2,3]	[false,false,true]	0

print(solution([4,7,12],[True,False,True]))
