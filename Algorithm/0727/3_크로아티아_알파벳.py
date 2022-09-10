dic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in dic :
    word = word.replace(i, '*')  
    #print(word)
print(len(word))