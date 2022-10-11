n, k = map(int, input().split())

n_list = list(map(int, input().split()))
m_list = []
for i in range(1, n):
    m_list.append(n_list[i] - n_list[i - 1])
# m_list.sort(reverse=True)
m_list.sort()
# print(m_list)

print(sum(m_list[: k - 1]))
