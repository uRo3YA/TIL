daehak=list(map(int,input().split()))
if sum(daehak)>=100:
    print("OK")
else:
    min_a=min(daehak)
    for i in range(len(daehak)):
        if daehak[i]==min_a:
            if i==0:
                print("Soongsil")
            elif i==1:
                print("Korea")
            elif i==2:
                print("Hanyang")

            