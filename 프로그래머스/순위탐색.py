from collections import defaultdict # key가 비어있는 경우를 위해 사용
from itertools import combinations

def solution(info, query):
    answer = []
    _dict = defaultdict(list)
    for i in info: # _dict에  value로 넣기 위해 사람들의 데이터에서 점수를 따로 빼낸다.
        data = i.split(' ')
        score = int(data[-1])
        data = data[:-1]
        for n in range(5):
            for c in combinations(data, n): # 한 사람의 데이터에서 만들수 있는 모든 조합을 _dict에 key로 넣는다
                key = ''.join(c)
                _dict[key].append(score)
    for value in _dict.values():
        value.sort()

    for q in query: # 쿼리를 하나씩 분해해서 and와 '-'을 없애고 문자열만 있게끔 가공한다.
        q = q.split(' ')
        point = int(q[-1])
        q = q[:-1]
        q = ''.join(q)
        q = q.replace('-', '')
        q = q.replace('and', '')
        # print('q: ', q)
        if q in _dict: # 한 사람의 데이터의 모든 조합인 _dict에 하나의 쿼리라도 해당이 되면 점수를 scores에 넣는다.
            scores = _dict[q] 
            # print('score: ', scores)
            # print('point: ', point)
            if len(scores) > 0: # 점수가 1개라도 있으면
                left, right = 0, len(scores) # lower bound 이용해서 인덱스 찾기    
                while left < right:
                    mid = (left + right) // 2        
                    if scores[mid] >= point:
                        right = mid
                    else:
                        left = mid + 1
                answer.append(len(scores) - left) # 기준에서부터 오른쪽에 있는 값들의 개수만큼 answer에 넣는다
        else:
            answer.append(0)
    return answer