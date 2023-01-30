N, new, P = map(int, input().split())
score = []
if N:
	score = list(map(int, input().split()))
	score.append(new)
	score.sort(reverse=True)
	rank = score.index(new) + 1
	if rank > P:
		print(-1)
	else:
		if N == P and new == score[-1]:
			print(-1)
		else:
			print(rank)
else:
	print(1)