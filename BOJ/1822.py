n, m = map(int, input().split())
n_list = set(map(int, input().split()))
m_list = set(map(int, input().split()))

res = n_list - m_list
if res != 0:
    print(len(res))
    print(*sorted((list(res))))
else:
    print(0)
