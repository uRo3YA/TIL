import sys
input=sys.stdin.readline
trees={}
tree_num=0
while True:
    try:
        tree=input().rstrip()
        if tree=="":
            break
        tree_num+=1
        if tree in trees:
           trees[tree] += 1
        else:
            trees[tree] = 1
    except EOFError:
        break

sorted_trees = sorted(trees.items(), key=lambda x:x[0])
for k, v in sorted_trees:
    percentage = round((v/tree_num)*100, 4)
    print(k, '%.4f' %percentage)
# import sys

# total = 0
# dic = dict()
# while 1:
#     word = sys.stdin.readline().rstrip()
#     if word == '':
#         break
#     total += 1   
#     if word in dic:   # 전에 이미 나왔으면
#         dic[word] += 1
#     else:
#         dic[word] = 1
# sdic = dict(sorted(dic.items()))
# for i in sdic:
#     a = sdic[i]
#     per = (a / total * 100)
    
#     print("%s %.4f" %(i, per))