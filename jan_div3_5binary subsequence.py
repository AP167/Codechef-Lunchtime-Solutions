try:
    t=int(input())
    for i in range(t):
        n=int(input())
        s=input()
        one=s.count("1")
        l=[one,n-one]
        o=one
        j=n-1
        rem=0
        check=1
        while j>=0 :
            if s[j]=="0" :
                rem=rem+1
            else :
                break
            j=j-1
        while j>=0 :
            if check==1:
                if s[j]=="1":
                    o=o-1
                else:
                    l.append(rem+o)
                    check=0
            elif check==0 :
                if s[j]=="0" :
                    rem=rem+1
                else :
                    check=1
            j=j-1
        print(min(l))
except :
    pass

