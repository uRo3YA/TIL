from operator import index
import sys

sys.stdin = open("_조교의성적매기기.txt")
# 10 개의 평점을 총점이 높은 순서대로 부여하는데,
# ["A+" ,"A0" ,'A-' ,'B+' ,'B0' ,'B-' ,'C+' ,'C0' ,'C-' ,'D0']
# 각각의 평점은 같은 비율로 부여할 수 있다.
# 예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.
# 총점 =중간 (35%) + 기말(45%) + 과제 (20%)
# 입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,
# 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
# K 번째 학생의 학점을 출력하는 프로그램을 작성하라.

# [제약사항]
# 1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)
# 2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)
# 3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
# 테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
grade=["A+" ,"A0" ,'A-' ,'B+' ,'B0' ,'B-' ,'C+' ,'C0' ,'C-' ,'D0']
for tc in range(1, int(input())+1):
    n,k=map(int,input().split())
    
    student_list=[]
    for n_1 in range(n):
        exam1,exam2,work=map(int,input().split())
        total=(exam1*0.35)+(exam2*0.45)+(work*0.2)
        student_list.append(total)
    #N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.
  
    k_score = student_list[k-1]
    student_list.sort(reverse=True)

    rank_of_ten = student_list.index(k_score) // (n//10) 
    print(f"#{tc}", grade[rank_of_ten])# end = " ")