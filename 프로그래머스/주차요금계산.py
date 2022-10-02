from collections import defaultdict
import math

# 시각, 번호판, 상태


def dateToMinutes(date):
    h, m = map(int, date.split(":"))
    return h * 60 + m


def solution(fees, records):
    answer = []
    park_time = {}
    park_total_time = defaultdict(list)
    s_time = fees[0]
    s_fee = fees[1]
    m_time = fees[2]
    m_fee = fees[3]
    for r in records:
        t, n, s = r.split()
        # 일반적인 입출차 케이스 시간 계산
        if s == "IN":
            park_time[n] = t
        elif s == "OUT":
            try:
                park_total_time[n] += dateToMinutes(t) - dateToMinutes(park_time[n])
            except:
                park_total_time[n] = dateToMinutes(t) - dateToMinutes(park_time[n])
            del park_time[n]
    # 23:59 기준으로 남아있는 차량들 전부 출차해서 시간 추가
    for car, minute in park_time.items():
        try:
            park_total_time[car] += 23 * 60 + 59 - dateToMinutes(minute)
        except:
            park_total_time[car] = 23 * 60 + 59 - dateToMinutes(minute)
    # 요금 계산 하기
    total_fees = {}

    for num, times in park_total_time.items():
        # 기본 시간보다 빨리 빠진 차는 기본요금으로 추가
        if times > s_time:
            # 요금 = 기본요금+ 올림[(출차시간-기본시간)/단위시간] * 단위 요금
            total_fees[num] = int(s_fee + math.ceil((times - s_time) / m_time) * m_fee)
        else:
            total_fees[num] = int(s_fee)
    # 차량 기준으로 정렬 시키기
    a = dict(sorted(total_fees.items(), key=lambda x: x[0]))
    # 정답에 맞게 리스트 추가
    for num, f in a.items():
        answer.append(f)
    return answer


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

print(solution(fees, records))

# 각 차량별 총 시간

# 요금 계산= 기본 주차비+[주차시간-기본 주차시간]*[][단위 시간당 주차비]
# 5000 + ⌈(334 - 180) / 10⌉ x 600
