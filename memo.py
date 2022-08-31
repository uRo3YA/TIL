
num_moves = int(input())  # 표본 모양수열 길이
sample_form = list(map(int, input().split()))  # 표본 모양수열
num_shapes = int(input())  # 모양수열 갯수
shapes = []  # 모양수열 담을 리스트
for _ in range(num_shapes):
    shapes.append(list(map(int, input().split())))

# 1,3 / 2,4 매핑할 dict
reverse = {1:3, 2:4, 3:1, 4:2}
sames = []
for shape in shapes:
    reverse_shape = list(map(lambda x: reverse[x], shape))[::-1]  # 1,3 / 2,4 매핑 후 순서 뒤집기
    
    if shape == sample_form or reverse_shape == sample_form:
        sames.append(shape)
        continue
    
    # 십자카드 문제와 같은 풀이방법
    for i in range(1, num_moves):
        tmp = shape[i:] + shape[:i]
        reverse_tmp = reverse_shape[i:] + reverse_shape[:i]
        if tmp == sample_form or reverse_tmp == sample_form:
            sames.append(shape)
            break

print(len(sames))
for s in sames:
    print(' '.join(list(map(str, s))))