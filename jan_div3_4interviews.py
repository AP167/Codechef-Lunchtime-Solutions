import math
try :
    t=int(input())
    for i in range(t):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        corr=0
        bot=1
        slow=0
        for j in range(n):
            if a[j]!=-1 :
                corr=corr+1
            if a[j]==-1 or a[j]>1 :
                bot=0
            if a[j]>k :
                slow=1
        if corr<math.ceil(n/2) :
            print("Rejected")
        elif slow==1 :
            print("Too Slow")
        elif bot==1 :
            print("Bot")
        else :
            print("Accepted")
except :
    pass
