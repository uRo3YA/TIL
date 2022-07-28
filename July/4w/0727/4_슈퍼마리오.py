score=0
for i in range(10):
    n=int(input())
    score+=n
    if score>=100:
        if score-100 > 100 - (score -n):
            score-=n
        break
print(score)

#  if score>=100:
# #         if 108> 100 - (score -n):
# #             score-=n