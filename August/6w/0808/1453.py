n=int(input()) # 사람수
num_list=[] #일단 빈 배열
num_list=list(map(int,input().split())) #정수로 리스트 입력
s_list=[0]*101 # 자리 초기화
jungbok=0

for i in num_list:          #손님 리스트 순서대로
    if s_list[i] != 0:      #리스트에 있는 정수값을 자리 조회
        jungbok += 1        #0이 아니면 중복 추가 
    else:
        s_list [i] += 1     #0= 아직 사람이 안왔으니 1로 채움  

print(jungbok)
