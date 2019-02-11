n,k=raw_input().split()
if int(n)>0:
    res=1
    for i in range(0,int(k)):
        res=res*int(n)
        print res
else:
    print 0
