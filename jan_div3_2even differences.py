try :
    t=int(input())
    for i in range(t) :
        n=int(input())
        a=list(map(int,input().split()))
        odd=0
        even=0
        for j in range(n):
            if a[j]%2==0 :
                even=even+1
            else :
                odd=odd+1
        if even>=odd :
            print(odd)
        else :
            print(even)
except :
    pass
