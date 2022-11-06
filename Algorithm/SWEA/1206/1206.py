import sys

sys.stdin = open('1206.txt')

for tc in range(1,11):
    l=int(input())
    arr=list(map(int,input().split()))
    view=0
    for i in range(2,l-2):
        front_view_2 = arr[i] - arr[i-2] #두칸 앞의 빌빙과 비교 
        front_view_1 = arr[i] - arr[i-1]  #한칸 앞의 빌딩과 비교
        back_view_1 = arr[i] - arr[i+1] #한칸 뒤의 빌딩과 비교
        back_view_2 = arr[i] - arr[i+2]#두칸 뒤의 빌딩과 비교
        if front_view_2 > 0 and front_view_1 > 0 and back_view_1 > 0 and back_view_2 > 0 : # 모든 조망권이 확보 됐을때
            view += min(front_view_2, front_view_1, back_view_1, back_view_2) # 조망권이 확보된 수
    print(f"#{tc}:",view)