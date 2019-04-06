import random
def juger(lisn,a,i,n):
    if ((i>=1 and abs(lisn[i-1]-a)==1) or (i>=n and abs(lisn[i-n]-a)==1)):
        x=0
    else: x=1
    return x
        
def schulte(n):
    max=n*n
    ori=list(range(1,max+1))
    random.shuffle(ori)
    test=list()
    i=0
    while i<max:
        while (juger(test,ori[0],i,n)==0):
            random.shuffle(ori)
        test.append(ori[0])
        del ori[0]
        i+=1
    i=0
    print ('-'*25)
    while i<max:
        print ('|\t',end='')
        for x in test[i:i+n]:
            print (x,'\t',end='')
        print ('|')
        i+=n
    print ('-'*25)

schulte(5)