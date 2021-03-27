try :
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        odd=0
        for j in range(n):
            if a[j]%2==1 :
                odd=odd+1
        if odd%2==1 :
            print(2)
        else :
            print(1)
except :
    pass
