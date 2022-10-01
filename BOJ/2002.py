N = int(input())
answer = 0
enter, out = dict(), []
for i in range(N):
    car = input()
    enter[car] = i
for _ in range(N):
    car = input()
    out.append(car)

for i in range(N - 1):
    for j in range(i + 1, N):
        # 추월한만큼 순서가 밀림
        # 입구 순서가 그 뒤에 있는 차량들에 입구 순서보다 늦은 순서
        if enter[out[i]] > enter[out[j]]:
            answer += 1
            print("추월한 차, 추월 당한 차:", out[i], out[j])
            break
print(answer)
